#FROM python:3.11
#FROM python:3.11.9-slim-bullseye
#FROM python:3.11.9-alpine3.20
#FROM datamario24/isdomi:0.8.3
FROM datamario24/python311scikitlearn-fastapi:1.0.0
WORKDIR /code

#COPY ./requirements.txt /code/requirements.txt 
COPY src/fishmlserv/main.py /code/
#COPY requirements.txt /code/
COPY /src/fishmlserv/model/get-model-path.py /code/
COPY /src/fishmlserv/knn_pred.py /code/

# 모델 서빙만 (의존성 위 BASE 이미지에서 모두 설치했다.)
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --no-cache-dir --upgrade git+https://github.com/mangG907/fishmlserv.git@1.1/find_k
RUN chmod +x /code/get-model-path.py
RUN ln -s /code/get-model-path.py /usr/local/bin/get-model-path
RUN chmod +x /code/knn_pred.py
RUN ln -s /code/knn_pred.py /usr/local/bin/prediction

# 모델 서빙을 위해 API 구동을 위한 FastAPI RUN
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
