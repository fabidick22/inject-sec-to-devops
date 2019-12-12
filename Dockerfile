FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY . /app
COPY ./requirements.txt /var/www/requirements.txt

ENV FLASK_ENV=dev
#RUN apt-get remove -y libjpeg*


RUN pip install -r /var/www/requirements.txt