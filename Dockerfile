FROM python:3.7

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./application /code/application

#
CMD ["uvicorn", "application.src.main:app", "--host", "0.0.0.0", "--port", "80"]