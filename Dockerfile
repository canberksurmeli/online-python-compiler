FROM python:alpine3.8

COPY . ./usr/src/app
WORKDIR /usr/src/app
RUN apt update
RUN apt install graphviz -y
RUN pip install -r requirements.txt