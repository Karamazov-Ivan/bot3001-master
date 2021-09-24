FROM python:3.9

WORKDIR /Documents/bot300


ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -U pip aiogram pytz && apt-get update && apt-get install sqlite3 && pip install requests && pip install bs4
COPY . .


ENTRYPOINT ["python", "telegram300.py"]

