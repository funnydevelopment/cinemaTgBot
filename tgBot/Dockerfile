FROM python:3.11-slim-buster

RUN useradd wagtail

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /app
COPY bot.py .
COPY config ./config
COPY src ./src

USER wagtail