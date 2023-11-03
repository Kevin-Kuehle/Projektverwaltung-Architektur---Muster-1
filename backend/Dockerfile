FROM python:3.11.4-alpine

# Set work directory
WORKDIR /usr/src/app

# prevent python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# prevent python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN pip install djangorestframework
RUN pip install django-cors-headers


COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY . /usr/src/app

