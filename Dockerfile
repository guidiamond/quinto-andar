FROM tensorflow/tensorflow:latest-gpu
RUN mkdir /app
ADD train.py /app
ADD requirements.txt /app
WORKDIR /app
VOLUME /app

RUN pip install --upgrade pip

RUN pip install --user -r requirements.txt


CMD python ./quintoandar/quinto-andar/train.py
