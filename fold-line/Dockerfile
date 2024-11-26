FROM ubuntu:20.04

RUN mkdir /challenge && \
    chmod 700 /challenge

COPY cipher.txt /app/
COPY flag.txt /app/
WORKDIR /app

RUN tar czvf /challenge/artifacts.tar.gz cipher.txt && \
    echo "{\"flag\":\"$(cat flag.txt)\"}" > /challenge/metadata.json

# keep the container running
CMD ["tail", "-f", "/dev/null"]
