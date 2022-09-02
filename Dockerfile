FROM python:3.9-slim-buster

WORKDIR /lunchplace

COPY requirements.txt requirements.txt
COPY /lunchplace/ .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary
RUN pip install --upgrade djangorestframework-simplejwt


COPY . .
RUN echo "$PWD"
CMD [ "python", "manage.py" , "runserver"]