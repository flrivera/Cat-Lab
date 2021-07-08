<img src="Title_1.png" alt="hi" class="inline"/>
## Approximately 67% of households have pets in the United States, yet toxicity levels of common flowers are not readily available. 

Pet-Lab will:
- Identify the flower type depending on unique charasteristics.
- Search database to provide user with toxicity information (severity, common symptoms) as well as flower description to aide in detection confirmation.


## Existing products and gap in the Market

| <img src="apcc.PNG" alt="hi" class="inline"/>        |
| -------------- |
| APCC by the ASPCA does have information about the toxicity of plants and flowers but lacks identification capabilities.   |



**Some of the most common complaints about APCC are as follows:**
- Poor pictures of plants/ dont know what plants I have are called
- Listings by common not latin names
- Doesnt say how much would be toxic
- The contact number to poison control charges a fee.
- Small amount of plants and hasn't been updated since 2015.
- Doesn/t have flowers commonly used in essential oils.
- “Much to exact. Recognizes almond but not almonds. Does not recognize anything    with a trailing space.
- Weeds,  You have plants but nothing about weeds which dogs are more likely to eat.


## Target Goals

<img src="Slide1.jpg" />


## Explaratory Data Analysis

### Average images, Contrast of Images and PCA of the 5 most common classes (rose, dandelion, daisy, tulip, sunflower)

      
 <p float="left">
  <img src="Averages.png" width="33%"  height="250"/>
  <img src="contrast_small.png" width="33%" height="250" /> 
  <img src="dandelion_Eigenstate-1.png" width="33%" height="250"/>
</p>

### Getting features of the 5 most common classes

<p float="center">
  <img src="pairplot.png" width="60%"  height="400"/>
</p>
 

#### Fitting and making predictions
<p float="center">
      <img src="SVC_linear.png" width="60%" height="400"/>
</p>

kNN(k=3) accuracy is : 0.87

NB accuracy: 0.91

dtree accuracy: 0.91

Random Forrest accuracy: 0.91

