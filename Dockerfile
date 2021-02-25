FROM python:3.8.3-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

ADD . /code
WORKDIR /code

COPY docker-entrypoint.sh /
ENTRYPOINT ["sh", " /docker-entrypoint.sh"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir