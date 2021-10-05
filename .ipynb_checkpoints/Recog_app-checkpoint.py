import os
from natsort import natsorted, ns
from skimage import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from tempfile import NamedTemporaryFile
import requests
import json 
import pickle
import streamlit as st
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import toxicity as toxic
from PIL import Image
from dotenv import load_dotenv
from urllib.error import URLError


from io import BytesIO


load_dotenv() # load my enviornment variables

API_key=os.getenv('API_key')

st.title('Freida Rivera')
st.title('TDI-Capstone')


st.title('Pet-Lab: Keep your pets safe! Upload a picture and obtain a flowers toxicity information with the click of a button.')

#upload user Image

#st.sidebar.header("Image Classification")

st.set_option('deprecation.showfileUploaderEncoding', False)
fileUpload = st.file_uploader("Choose a file (jpg or png only)", accept_multiple_files=False,type = ['jpg', 'png','JFIF'])



temp_file = NamedTemporaryFile(delete=False)



#Reformat Image

def img2np( filename, size = (64, 64)):
    # iterating through each file
    #st.write(list_of_filename)

    current_image = image.load_img(filename, target_size = size,color_mode = 'grayscale')
    # covert image to a matrix
    img_ts = image.img_to_array(current_image)
    #st.write(img_ts)
    # turn that into a vector / 1D array
    img_ts = [img_ts.ravel()]
    try:
      #  st.write(hi)
        # concatenate different images
        full_mat = np.concatenate((full_mat, img_ts))

    except UnboundLocalError: 
        #st.write(hi)
        # if not assigned yet, assign one
        full_mat = img_ts
       

    return full_mat


#Get feature of image

def find_mean_img(full_mat,size = (64, 64)):
    mean_img = np.mean(full_mat, axis = 0)

    mean_img = mean_img.reshape(size)

    return mean_img




def find_std_img(full_mat,size = (64, 64)):
    # calculate the average
    std_img = np.std(full_mat, axis = 0)
    # reshape it back to a matrix
    std_img = std_img.reshape(size)

    return std_img



#run feature code


if fileUpload is not None:
    #st.write('hi')
    image1 = Image.open(fileUpload)
    st.image(image1, caption='Uploaded Image.', width=None)
    st.write("")
    
    temp_file.write(fileUpload.getvalue())


    full_mat_upload=img2np(temp_file.name, size = (64, 64))
    mean_upload=find_mean_img(full_mat_upload)
    std_upload=find_std_img(full_mat_upload)
    
#flatten upload_features

#&

# make feature dataframe.

upload_feature_dataframe=pd.DataFrame(columns = ['mean','std'])
upload_feature_dataframe['mean']=mean_upload.flatten()
upload_feature_dataframe['std']=std_upload.flatten()

#st.write(upload_feature_dataframe)

#upload ML_Model:
filename='5_flowers_knn.sav'
Loaded_model_1=loaded_model = pickle.load(open(filename, 'rb'))




st.title("Classifications")
#
Predictions=Loaded_model_1.predict_proba(upload_feature_dataframe)

Classification=pd.DataFrame(Predictions,columns= [f'{el}' for el in Loaded_model_1.classes_])

#st.write('Prob Daisy:',Classification['daisy'].mean())
Probabilities=[Classification['daisy'].mean(),Classification['dandelion'].mean(),Classification['rose'].mean(),Classification['sunflower'].mean(),Classification['tulip'].mean()]


Flowers_to_Scrape=[]
for i in range(0,len(Probabilities)):

    if Probabilities[i]>0:
        Flowers_to_Scrape.append(Loaded_model_1.classes_[i])
        st.write(f'Prob {Loaded_model_1.classes_[i]}',Probabilities[i])



# Pull Rover info! if prob > 0


    #pull rover info
    
    
st.title("Toxicity Information")

st.write()

pd.set_option('display.max_colwidth', 0)

Toxic_info=toxic.Get_Output(toxic.Search_flower_url_name(Flowers_to_Scrape))

Toxic_info.style.set_properties(subset=['Toxicity'], **{'width': '1000px'})
Toxic_info.style.set_properties(subset=['URL'], **{'width': '200px'})

st.write('For Class in substring of Flower')

st.dataframe(Toxic_info)


Toxic_info2=toxic.Get_Output(toxic.Search_flower_url_name(Flowers_to_Scrape,total_equality=True))

st.write('For Class exactly equal to Flower')
st.dataframe(Toxic_info2)


with st.beta_expander("Under the Hood"):
    
    st.title("Features")
#

    
    Image_scatter=Image.open("pairplot.png")
    st.image(Image_scatter)
    Image_violin=Image.open('violinplot.png')
#st.write(scatter)
    st.image(Image_violin)
#plot feature sns  st.write(scatter) overlay   upload values
     





