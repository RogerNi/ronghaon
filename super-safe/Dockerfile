FROM python:3.9-slim

RUN mkdir /challenge && \
    chmod 700 /challenge

WORKDIR /challenge

COPY app.py init_db.py /challenge/

RUN pip install Flask cryptography
RUN python init_db.py

ARG FLAG
RUN echo $FLAG | sed "s/.*{/picoCTF{n0t_sa3f_a7_a11_/1" > flag.txt
RUN echo $FLAG | sed "s/.*{/picoCTF{n0t_sa3f_a7_a11_/1" > secret_key.txt
RUN echo "{\"flag\":\"$(cat flag.txt)\"}" > /challenge/metadata.json
RUN tar czvf /challenge/artifacts.tar.gz app.py

EXPOSE 5000
# PUBLISH 5000 AS web
CMD ["python", "app.py"]
