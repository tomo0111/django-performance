FROM python:3.6.0

ENV PYTHONUNBUFFERED=1
ENV DB_HOST=
ENV DB_NAME=test
ENV DB_USER=root
ENV DB_PASS=

RUN mkdir -p /opt/django-performance

WORKDIR /opt/django-performance

ADD requirements.txt /opt/django-performance

RUN pip install -r requirements.txt

ADD . /opt/django-performance/

CMD python manage.py makemigrations
CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000