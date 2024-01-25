FROM python:3.11.6
LABEL authors="KarmaSherpa"

WORKDIR /app

COPY . /app

ENV PYTHONPATH=/app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD "python" "app.py"