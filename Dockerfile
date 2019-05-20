FROM python:3.6-alpine

#Create app directory
WORKDIR /usr/src/app

#Copy files
COPY ./scripts ./

#Install app dependencies
RUN apk update && apk add gcc musl-dev libffi-dev openssl-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["python", "webhook.py"]