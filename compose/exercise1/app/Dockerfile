FROM python:3.10-alpine

WORKDIR /src/app

RUN --mount=type=bind,src=requirements.txt,target=requirements.txt \
    pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY app.py app.py

CMD ["flask","run"]
