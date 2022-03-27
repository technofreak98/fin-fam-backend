FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y apt-utils libpq-dev libgl1-mesa-dev python-dev gcc && \
    apt-get install -y python3-pip libglib2.0-0 libsm6 libxext6 libxrender1

RUN pip3 install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt && \
    pip3 install -U pip-licenses && pip-licenses

ADD ./modules/. ./modules/
ADD ./database.py ./database.py
ADD ./app.py ./app.py

EXPOSE 5000

CMD ["python3", "app.py"]