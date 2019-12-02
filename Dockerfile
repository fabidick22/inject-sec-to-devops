FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY . /app
COPY ./requirements.txt /var/www/requirements.txt

RUN pip install -r /var/www/requirements.txt