FROM python:3.7.5-alpine

WORKDIR /viper

RUN apk --update-cache\
            add bash\
            gcc\
            g++\
            musl

COPY requirements.txt /viper

RUN pip install -r requirements.txt
ENTRYPOINT sh