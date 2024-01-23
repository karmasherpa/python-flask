FROM python:3.11.6
LABEL authors="KarmaSherpa"

WORKDIR /app

COPY . /app

RUN cd /app && pip install -r requirements.txt

ENV PYTHONPATH=/app

EXPOSE 5000


CMD "python" "main.py"