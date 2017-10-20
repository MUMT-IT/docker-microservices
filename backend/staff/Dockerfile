FROM python:2

WORKDIR /app
COPY requirements.txt requirements.txt
COPY app/main.py /app/main.py
RUN pip install -r requirements.txt
EXPOSE 5440

CMD ["python", "main.py"]