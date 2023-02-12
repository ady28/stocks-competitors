FROM python:3.11.2-alpine3.17

RUN apk add --no-cache expat=2.5.0-r0

WORKDIR /usr/src/app

ENV PORT=8080 \
    MONGO_PORT=27017 \
    MONGO_NAME=lnx1 \
    MONGO_DB=stocks \
    STOCKS_APP_ENV=test

EXPOSE $PORT

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir urllib3==1.26.5 -U

COPY . .

USER nobody

CMD [ "python", "./main.py" ]