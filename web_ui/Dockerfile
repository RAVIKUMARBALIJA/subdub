FROM python:3.6.15

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV DISPLAY=:99

# Install apt dependencies
RUN apt update && apt install -y openjdk-11-jdk && export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64


# Install requirements
COPY . /app

RUN pip install -r setup/requirements.txt
EXPOSE 5000

ENTRYPOINT python wsgi.py