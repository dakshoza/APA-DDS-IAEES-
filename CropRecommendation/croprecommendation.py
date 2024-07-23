import numpy as np
from collections import Counter
import pickle
from models.DeepNN.DeepNN import cropRecModel

NNmodel = cropRecModel()

def predictCrop(n :int, p :int, k :int, temperature :int, humidity: int, ph:float, rainfall: int):
    """
    json template
    {
  "n": 10,
  "p": 40,
  "k": 20,
  "temp": 20,
  "humidity": 10,
  "ph": 6.5,
  "rainfall": 1
}

    """
    with open('./models/KNN.pkl', 'rb') as f:
        KNN = pickle.load(f)
    with open('./models/NaiveBayes.pkl', 'rb') as f:
        NB = pickle.load(f)
    with open('./models/RandomForest.pkl', 'rb') as f:
        RF = pickle.load(f)
    with open('./models/SVMClassifier.pkl', 'rb') as f:
        SVM = pickle.load(f)
    # Create input data array 
    data = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
    prediction1 = KNN.predict(data)
    prediction2 = NB.predict(data)
    prediction3 = RF.predict(data)
    prediction4 = SVM.predict(data)
    prediction5 = NNmodel.getPrediction(data)

    predictions = [prediction1[0], prediction2[0], prediction3[0], prediction4[0], prediction5]
    print(predictions)

    vote_counts = Counter(predictions)

    if all(count == 1 for count in vote_counts.values()):
      return prediction5
    else:
      return vote_counts.most_common(1)[0][0]
      
input_values = {
  "n": 77,
  "p": 49,
  "k": 42,
  "temperature": 20,
  "humidity": 82,
  "ph": 6.5,
  "rainfall": 202
}

prediction = predictCrop(**input_values)
print(prediction)


