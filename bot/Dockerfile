FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=settings
ENV DJANGO_ALLOW_ASYNC_UNSAFE=true

CMD [ "python", "bot.py" ]