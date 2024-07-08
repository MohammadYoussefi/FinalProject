FROM python:3.12.2


COPY requirements.txt .


RUN python -m pip install -r requirements.txt

WORKDIR /app

COPY sql_app .
COPY sql_app/Main.py .

CMD [ "uvicorn",  "Main:app", "--host", "0.0.0.0", "--port", "8000"]
