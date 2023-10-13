FROM docker.io/library/python:3.11-slim

RUN pip install -U pip && pip install gunicorn

RUN mkdir /app

COPY ./ /app

RUN cd /app && pip install .

CMD gunicorn -b 0.0.0.0:8050 caesar.gaius:julius
