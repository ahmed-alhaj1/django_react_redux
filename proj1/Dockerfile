#pulll base image 

FROM python:3.8

#set enviroment variables
#prevents python from writing pyc files to disk

ENV PYTHONDONTWRITEBYTECODE 1

# prevents python from buffering stdout and stderr 

ENV PYTHONUBUFFERED 1

# set work directory 

RUN mkdir /code 

WORKDIR /code

# install dependancies

RUN pip install pipenv

COPY Pipfile Pipfile.lock /code/

RUN pipenv install --system

copy ./code/

