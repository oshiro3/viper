FROM python:3.7.5-alpine

WORKDIR /viper

RUN apk add bash gcc

ADD test /viper/test
ADD viper /viper/viper
ADD .gitignore /viper
ADD inspect.sh /viper
ADD requirements.txt /viper
ADD sample.py /viper
ADD sample_2.py /viper

#RUN pip install -r requirements.txt