FROM python:3.10

COPY requirements.txt /temp/requirements.txt
COPY . service

WORKDIR /service

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user
USER service-user