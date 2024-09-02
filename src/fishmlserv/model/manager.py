import os
import pickle

#def get_model_path():
    # import os ...
    # 이 함수 파일의 절대 경로를 받아온다.
    # 절대 경로를 이용해 model.pkl의 경로를 조합
    # 조합된 경로를 리턴 = 끝

    # 사용 fastapi main.py 에서 아래와 같이 사용
    # from fishmlserv.model.manager import get_model_path
    #return "wanna go home"


def get_model_path():
    #path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.dirname(__file__)
    model_path = path + "/" + "model.pkl"
    with open(model_path, 'rb') as f:
        fish_model = pickle.load(f)
    return fish_model
print(get_model_path())
