FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY . /app
COPY ./requirements.txt /var/www/requirements.txt

RUN apt-get update && apt-get install -y \
    libjpeg-turbo \
    mercurial

RUN pip install -r /var/www/requirements.txt