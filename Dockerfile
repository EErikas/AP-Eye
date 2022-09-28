# Stored in Docker Hub as eerikas/resmon
FROM python:3.9
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
CMD [ "python", "app.py" ]