FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./src/ /app/src
COPY ./setup.py /app/setup.py
COPY ./start.py /app/start.py

WORKDIR /app

ENV GIT_USER <YOUR_GIT_USERNAME>
ENV GIT_PASS <YOUR_GIT_ACCESS_KEY>

RUN pip install .