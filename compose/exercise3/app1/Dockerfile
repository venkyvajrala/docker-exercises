FROM python:3.10-alpine

WORKDIR /src/app

RUN --mount=type=bind,src=requirements.txt,target=requirements.txt \
    pip install -r requirements.txt

COPY app.py app.py
COPY templates/ templates/

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app.py

CMD [ "flask", "run" ]
