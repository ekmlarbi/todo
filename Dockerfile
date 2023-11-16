FROM python:3.9-alpine

RUN apk update && apk add build-base postgresql-dev

ENV INSTALL_PATH /todo
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -c "python:config.gunicorn" "todo.app:create_app()"
