[](https://share.streamlit.io/flrivera/pet-lab/main/Recog_app.py)

[](https://petlab.s3.us-east-2.amazonaws.com/5_flowers_trial.zip)


# Pet-Lab:
###  Flower Classification and Toxicity Information App
   
## Overview

Pet-Lab is an innovative application designed to help pet owners keep their pets safe. By simply uploading a picture of a flower, users can obtain toxicity levels with just a click of a button. The app identifies flowers based on unique characteristics, categorizing them into five types. It then searches a database to provide users with toxicity information, including severity and common symptoms, as well as a flower description to aid in detection confirmation.

## Table of Contents

•	[Installation](#installation)
•	[Usage](#usage)
•	[Features](#features)
•	[Contributing](#contribution)
•	[License](#license)

## Installation
Available through Streamlit.

Clone repo and use ‘streamlit run Recog_app.py’



## Project Structure
- **Recog_app_AWS_call.py**: uses s3fs to both save and retrieve ml models as zip files. Taken from https://gist.github.com/ramdesh keras_model_s3_wrapper.py
- **remove_image_background**: Contains functions for background removal using OpenCV. Python function that takes an image file path as input, removes the background of the image, and saves the resulting image with a transparent background. It utilizes the OpenCV library to perform image processing operations.
- **decode_and_resize.py**: Implements image decoding and resizing operations.
-	**toxicity.py**:  handles the web scrapping for pet toxicity info of classified flowers using https://www.aspca.org/pet-care/animal-poison-control/toxic-and-non-toxic-plants
- **Recog_app.py**: The main application file that integrates the functionalities from other files.

## Usage


1.	Upload a picture using the Pet-Lab app.
2.	Click the button to obtain toxicity levels.
3.	Receive information about the identified flower, including toxicity severity and common symptoms.

## Features

Pet-Lab offers the following key features:

•	Flower identification into 5 types based on unique characteristics.
•	Database search for toxicity information, including severity and symptoms.
•	Background removal of images.
•	Utilization of the Inception v3 architecture pretrained on ImageNet.

##  Contributing

We welcome contributions to enhance Pet-Lab. To contribute, follow these steps:
1.	Fork the project.
2.	Create a new branch (git checkout -b feature/your-feature).
3.	Commit your changes (git commit -m 'Add some feature').
4.	Push to the branch (git push origin feature/your-feature).
5.	Open a pull request.
6.	
## License
Pet-Lab is licensed under the MIT License - see the LICENSE file for details.

