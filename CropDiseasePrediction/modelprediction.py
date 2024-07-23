from imagemodel import imageModel

def makePrediction(image_dir):
    imgModel = imageModel()
    print(imgModel.predict_on_image(image_dir))

#  load image path
image_dir = "./test images/tomato early blight leaf (1).jpg"
makePrediction(image_dir)