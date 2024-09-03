#!/usr/bin/env python3
from sklearn.neighbors import KNeighborsClassifier
from fishmlserv.model.manager import get_model_path
import pickle
import fire
def knn_model(l:float, w:float):
    model_path = get_model_path()
    with open(model_path, 'rb') as f:
        fish_model = pickle.load(f)

    prediction = fish_model.predict([[l, w]])
    if prediction == 0:
        fish_name = "Bream"
    else:
        fish_name = "Smelt"
    print(f'이 물고기는 {fish_name}이다.')
    return fish_name
if __name__ == '__main__':
  fire.Fire(knn_model) # fire 쓰려면 있어야 한다네요..
