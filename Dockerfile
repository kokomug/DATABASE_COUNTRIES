FROM python:3.10

EXPOSE 5000

COPY requirements.txt .

RUN pip install -r requirements.txt


WORKDIR /app
COPY . .

ENV FLASK_APP=app.py


ENTRYPOINT ["gunicorn", "--bind","0.0.0.0:5000", "app:app"]