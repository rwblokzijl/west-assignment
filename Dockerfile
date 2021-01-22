FROM python:3.8-alpine

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache pcre-dev
RUN apk add --update --no-cache --virtual .tmp python3-dev build-base linux-headers pcre-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN adduser -D user

RUN mkdir /assignment
COPY ./src /assignment
WORKDIR /assignment
RUN chmod -R 755 /assignment

USER user

CMD ["uwsgi", "--http", ":8000", "--master", "--enable-threads", "--module", "assignment.wsgi"]

