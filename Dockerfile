FROM python:3.9.18-alpine
# Upgrade pip and setuptools to fix 
# CVE-2022-40897 and CVE-2023-5752 vulnerabilities⁠
RUN apk add --no-cache gcc musl-dev linux-headers python3-dev
RUN pip install --upgrade pip setuptools
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
CMD [ "python", "app.py" ]