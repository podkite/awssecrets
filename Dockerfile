FROM python:3.7.6-alpine3.11

WORKDIR /awssecrets
COPY . .
RUN python setup.py install

CMD ["awssecrets"]