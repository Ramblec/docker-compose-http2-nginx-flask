FROM python:3.9

RUN mkdir /var/www
WORKDIR /var/www

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
