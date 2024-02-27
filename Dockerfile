FROM python:3.10-slim

LABEL author="CLV"
COPY requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8080
CMD ["gunicorn", "--config", "config/GunicornConfig.py", "app:app"]