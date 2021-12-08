from selenium import webdriver
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import numpy as np
import itertools
from collections import defaultdict
from urllib.request import urlopen
import spacy
import requests
from spacy import displacy
from collections import Counter
from requests_futures.sessions import FuturesSession
from collections import deque
from ediblepickle import checkpoint
import os
import requests
import pandas as pd


#nlp = en_core_web_sm.load()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')   
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.aspca.org/pet-care/animal-poison-control/toxic-and-non-toxic-plants')
url2='https://www.aspca.org/pet-care/animal-poison-control/toxic-and-non-toxic-plants'

webpage= requests.get(url2)
soup = BeautifulSoup(webpage.text, 'lxml')
response=requests.get(url2);


def get_links(response):

    soup = BeautifulSoup(response.text,"lxml")
    links= soup.find_all('span', attrs={'class':'field-content'})

    return links


def get_link_href(el):
    main='https://www.aspca.org'
    url=el.find('a').get('href')
    real_url=main + url
    return(real_url)


def get_url_name_per_page(Links):
    Result=[]
    for i in range (len(Links)):

        if i%3==0:
            
            hrefs=get_link_href(Links[i])
            
            #Href.append(hrefs)
            list_o=(hrefs,str(hrefs[80:]).lower())
            
            Result.append(list_o)
           # Names.append(hrefs[80:])

    return(tuple(Result))




def get_page_args(i):
    
    if i==0:
        return {"url": url2}
    
    else:
        
        return {"url": url2,
            "params": {"page": i}}
    
 
session = FuturesSession(max_workers=5);
Pages_urls_plant_names = Pairs = [pairs 
         for future in [session.get(**get_page_args(i)) for i in range(69)]
         for pairs in get_url_name_per_page(get_links(future.result()))]
         




def get_plant_toxicity_info(url_name_tuples):
    
    
    URL=url_name_tuples[0]
    Name=url_name_tuples[1]


    response=requests.get(URL)
    
    
    
    soup=BeautifulSoup(response.text,"lxml")
    


    labels = soup.find_all('span', attrs={'class':'label-inline-format-label'})
    label_values = soup.find_all('span', attrs={'class':'values'})
    

        
    return(URL,Name,labels,label_values)



def Get_Output(Pages_urls_plant_names_in_search):
    pd.set_option('display.max_colwidth', 0)
    URL=[]
    Name=[]
    Labels=[]
    Label_Values=[]
    X=[]
    
   
    for i in range(len(Pages_urls_plant_names_in_search)):
        url_name_tuples=Pages_urls_plant_names_in_search[i]
        url,name,labels,label_values=get_plant_toxicity_info(url_name_tuples)
        label=[i.text.strip('\n') for i in labels]
        vals=[i.text.strip('\n') for i in label_values]
        URL.append(url)
        Name.append(name)
        
        Labels.append(label)
        Label_Values.append(vals)
     
    #print(Labels)
    for el in range(len(Labels)):
       # print(el)
        labels=Labels[el]
        vals=Label_Values[el]
       # print(vals)
        for i in range(len(labels)):

            if labels[i]=='Non-Toxicity:' or labels[i]=='Toxicity:' :
                #print('hi')
                #print(labels)
                labels=labels[i].strip(', ')
               
                Other=vals[i]
                #Others=np.array(Other.strip(','))
       
                
                X.append(Other)

        
    
  

    Result=pd.DataFrame()
    Result['URL']=URL
    Result['Name']=Name
    Result['Toxicity']=X
    #Result['Toxicity']=Result['Toxicity'].str.wrap(10000)
    Result.set_index('Name',inplace=True)
    #Result['URL']=URL
   # Data=(URL,Name,Labels,Label_Values,X)
    
    return(Result)
    
    
 ##########

def Search_flower_url_name(Labels,total_equality=False):
    if total_equality:
        Labels=[label.lower() for label in Labels]
        url_name_to_search=[]

        for label in Labels:
            for i in range (len(Pages_urls_plant_names)):
                if label == (Pages_urls_plant_names[i][1]):
                    url=Pages_urls_plant_names[i][0]
                    name=Pages_urls_plant_names[i][1]
                    add=(url,str(name))

                    url_name_to_search.append(add)
        
    else:
        Labels=[label.lower() for label in Labels]
        url_name_to_search=[]

        for label in Labels:
            for i in range (len(Pages_urls_plant_names)):
                if label in (Pages_urls_plant_names[i][1]):
                    url=Pages_urls_plant_names[i][0]
                    name=Pages_urls_plant_names[i][1]
                    add=(url,str(name))

                    url_name_to_search.append(add)
                    
                    
              #  else:
           #     url=Pages_urls_plant_names[i][0]
              #  add=(url,f'{label} not in database')
             #  url_name_to_search.append(add)
            
    return(url_name_to_search)

#Get_Output(Search_flower_url_name(Labels))
