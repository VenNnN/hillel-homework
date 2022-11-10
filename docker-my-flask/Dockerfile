FROM ubuntu:22.04
MAINTAINER VenN
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install Flask
COPY app.py /home/app.py
WORKDIR /home
ENTRYPOINT ["/usr/bin/python3", "./app.py"]