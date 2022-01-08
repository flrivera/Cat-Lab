---
layout: default
---
[](https://share.streamlit.io/flrivera/pet-lab/main/Recog_app.py)
[](https://flrivera-my-capstone-bucket.s3.us-east-2.amazonaws.com/my_model.zip)


## Approximately 67% of households have pets in the United States, yet toxicity levels of common flowers are not readily available. 


Pet-Lab will:
- Identify the flower type depending on unique charasteristics.
- Search database to provide user with toxicity information (severity, common symptoms) as well as flower description to aide in detection confirmation.


## Existing products and gap in the Market



|<img class="resize" src="apcc.PNG" width="10%" height="10%" > APCC by the ASPCA does have information about the toxicity of plants and flowers but lacks identification capabilities.   |


## How to tell different flowers apart?

### A simple example using the 5 most common classes (rose, dandelion, daisy, tulip, sunflower): 
We look for "features" or ways in which we can tell two different flowers apart using their pixel values

Below we have an average of the pixel values at each position of all the images for each flower (left), we can then use that to get the contrast between the average pixel values for each flower type (right), both of these can be used as features to tell the flowers apart.  

      
      
 <p float="left">
  <img src="Averages.png" width="48%"  height="250"/>
  <img src="Contrast.png" width="48%" height="250"/>
</p>

# Current and Future Developments

leh bleh bleh

