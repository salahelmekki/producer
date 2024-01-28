# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR ./app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install mysql dependencies
RUN apk update \
    && apk add --no-cache gcc make libc-dev python3-dev mariadb-dev

# install dependencies
RUN pip install -U pip setuptools wheel
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .
