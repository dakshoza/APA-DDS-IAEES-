# APA-DDS-IAEES-

To setup, follow the steps:

1. Clone the repository
2. Install requirements by running the command: ```pip install -r requirements.txt```

## Crop Disease Prediction

In the directory CropDiseasePrediction (access by using the command: ```cd CropDiseasePrediction```):

-> To run, run the modelprediction.py file using the following command: ```python modelprediction.py```. Note that you can change the input image path to test on different images. 

-> To investigate model training ipynb, access the file plant_disease_prediction_wheat_and_tomato.ipynb. The ipynb needs to be run on google colab, or you must install the necessary requirements locally. The dataset is present at: https://figshare.com/articles/dataset/Wheat_and_Tomato_Healthy_and_Disease_Images_Dataset/26357635

## Crop Recommendation 

In the directory CropRecommendation (access by using the command: ```cd CropRecommendation```):

-> To run, run the croprecommendation.py file using the following command: ```python croprecommendation.py```. Note that you can change the input values for testing.

-> In this directory, the models directory consists of the 5 models used. The DeepNN directory stores the weights, dataset (cropRecData.csv), model instantiating file for the code and the model training ipynb (DNN_Crop_Recommender.ipynb). The ipynb needs to be run on google colab, or you must install the necessary requirements locally. If running on google colab, upload the dataset to colab and update the path in ipynb for reading dataframe.

-> In this directory, the Notebooks folder consists of code taken from the repository: https://github.com/Phantom-Studiosad/Intelligent_CropPrediction_System/tree/main

