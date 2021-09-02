import os
from natsort import natsorted, ns
from skimage import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
import seaborn as sns





n_images=500
train_dir = 'Train' # image folder

# get the list of jpegs from sub image class folders
rose_imgs = [fn for fn in os.listdir(f'{train_dir}/rose') if fn.endswith('.jpg')]
tulip_imgs = [fn for fn in os.listdir(f'{train_dir}/tulip') if fn.endswith('.jpg')]
daisy_imgs = [fn for fn in os.listdir(f'{train_dir}/daisy') if fn.endswith('.jpg')]
sunflower_imgs = [fn for fn in os.listdir(f'{train_dir}/Sunflower') if fn.endswith('.jpg')]

dandelion_imgs = [fn for fn in os.listdir(f'{train_dir}/dandelion') if fn.endswith('.jpg')]

# randomly select 3 of each
select_rose = np.random.choice(rose_imgs, n_images, replace = False)
select_sunflower = np.random.choice(sunflower_imgs, n_images, replace = False)
select_tulip = np.random.choice(tulip_imgs, n_images, replace = False)
select_dandelion = np.random.choice(dandelion_imgs, n_images, replace = False)
select_daisy = np.random.choice(daisy_imgs, n_images, replace = False)

# plotting 2 x 3 image matrix
fig = plt.figure(figsize = (20,15))
for i in range(15):
    if i < n_images:
        fp = f'{train_dir}/rose/{select_rose[i]}'
        label = 'rose'
    elif i<2*n_images:
        fp = f'{train_dir}/sunflower/{select_sunflower[i-3]}'
        label = 'sunflower'
    elif i<3*n_images:
        fp = f'{train_dir}/tulip/{select_tulip[i-6]}'
        label = 'tulip'
    elif i<4*n_images:
        fp = f'{train_dir}/dandelion/{select_dandelion[i-9]}'
        label = 'dandelion'
    elif i<5*n_images:
        fp = f'{train_dir}/daisy/{select_daisy[i-12]}'
        label = 'daisy'

    
    # to plot without rescaling, remove target_size
    fn = image.load_img(fp, target_size = (100,100), color_mode='grayscale')




#DEfinitions
# making n X m matrix
def img2np(path, list_of_filename, size = (64, 64)):
    # iterating through each file
    for fn in list_of_filename:
        fp = path + fn
        current_image = image.load_img(fp, target_size = size, 
                                       color_mode = 'grayscale')
        # covert image to a matrix
        img_ts = image.img_to_array(current_image)
        # turn that into a vector / 1D array
        img_ts = [img_ts.ravel()]
        try:
            # concatenate different images
            full_mat = np.concatenate((full_mat, img_ts))
        except UnboundLocalError: 
            # if not assigned yet, assign one
            full_mat = img_ts
    return full_mat
    
    

def find_mean_img(full_mat, title, size = (64, 64)):
    # calculate the average
    mean_img = np.mean(full_mat, axis = 0)
    # reshape it back to a matrix
    mean_img = mean_img.reshape(size)
   # plt.imshow(mean_img, vmin=0, vmax=255, cmap='Greys_r')
   # plt.title(f'Average {title}')
   # plt.axis('off')
   # plt.savefig(f'Average {title}.pdf')
   # plt.show()
    
    return mean_img


def Contrast():
    Contrast_mean=[]
    Index=[]
    for i in range(0,len(categories)):
        for j in range(0,len(categories)):
            a=Mean[i]-Mean[j]
            Index.append([i,j])
            Contrast_mean.append(a)
            
    return Contrast_mean



def find_std_img(full_mat, title, size = (64, 64)):
    # calculate the average
    std_img = np.std(full_mat, axis = 0)
    # reshape it back to a matrix
    std_img = std_img.reshape(size)

    return std_img





categories=['rose','tulip','dandelion','daisy','sunflower']
Class=( 'rose','sunflower','tulip','dandelion','daisy')*64
Class2=( 'rose','sunflower','tulip','dandelion','daisy')*64




full_mat_rose=img2np(f'{train_dir}/rose/', rose_imgs, size = (64, 64))
full_mat_tulip=img2np(f'{train_dir}/tulip/', tulip_imgs, size = (64, 64))
full_mat_daisy=img2np(f'{train_dir}/daisy/', daisy_imgs, size = (64, 64))
full_mat_dandelion=img2np(f'{train_dir}/dandelion/', dandelion_imgs, size = (64, 64))
full_mat_sunflower=img2np(f'{train_dir}/sunflower/', sunflower_imgs, size = (64, 64))



rose_mean = find_mean_img(full_mat_rose, 'rose');
daisy_mean = find_mean_img(full_mat_daisy, 'daisy');
tulip_mean = find_mean_img(full_mat_tulip, 'tulip');
sunflower_mean = find_mean_img(full_mat_sunflower, 'sunflower');
dandelion_mean = find_mean_img(full_mat_dandelion, 'dandelion');


rose_std = find_std_img(full_mat_rose, 'rose')
daisy_std = find_std_img(full_mat_daisy, 'daisy')
tulip_std = find_std_img(full_mat_tulip, 'tulip')
sunflower_std = find_std_img(full_mat_sunflower, 'sunflower')
dandelion_std = find_std_img(full_mat_dandelion, 'dandelion')




Mean=[rose_mean,tulip_mean,dandelion_mean,daisy_mean,sunflower_mean]





def Feature_class():

    Pixel_means=[]
    Pixel_std=[]
   # PCA_Transform=[]

    j,k,l,m,o=0,0,0,0,0
    for i in range(len(Class)):

        if Class[i]=='rose':

            a=rose_mean.flatten()[i]
            b=rose_std.flatten()[i]
            #c=rose_pca.flatten()[i]
            j=j+1
        if Class[i]=='sunflower':
            a=sunflower_mean.flatten()[i]
            b=sunflower_std.flatten()[i]
            #c=sunflower_pca.flatten()[i]
            k=k+1
        if Class[i]=='tulip':
            a=tulip_mean.flatten()[i]
            b=tulip_std.flatten()[i]
            #c=tulip_pca.flatten()[i]
            l=l+1
        if Class[i]=='dandelion':
            a=dandelion_mean.flatten()[i]
            b=dandelion_std.flatten()[i]
            #c=dandelion_pca.flatten()[i]
            m=m+1
        if Class[i]=='daisy':
            a=daisy_mean.flatten()[i]
            b=daisy_std.flatten()[i]
           # c=daisy_pca.flatten()[i]
            o=o+1

        Pixel_means.append(a)
        Pixel_std.append(b)
        
    
    
    Features=Class2
    Features=pd.DataFrame(Features);


    Features=Features.rename(columns={0:'Class'});
    Features['Pixel_mean']= Pixel_means;
    Features['Pixel_std']= Pixel_std;
    
    return Features
    
    






#Plotting





def Plotting():
    

    Features_plot=Feature_class()

    





    sns_plot=sns.pairplot(Features_plot, hue="Class")
    sns_plot.savefig('pairplot.png')




    fig, ((ax1,ax2)) = plt.subplots(2,1, figsize=(7, 7))
    sns.violinplot(x="Class", y="Pixel_mean", data=Features_plot, ax=ax1)
    sns.violinplot(x="Class", y="Pixel_std", data=Features_plot, ax=ax2)
    

    plt.savefig('violinplot.png')
    
    
    return sns_plot,fig
    
    
    

    
    
    
    
    
    