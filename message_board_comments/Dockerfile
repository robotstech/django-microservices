FROM python:3.8-slim
MAINTAINER iamr0b0tx@livestocklog.com

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app

EXPOSE 8002

COPY ./requirements.txt /app/requirements.txt
RUN python -m pip install pip --no-cache-dir --upgrade
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["./entrypoint.sh"]
CMD ["gunicorn", "message_boards.wsgi", "-b 0.0.0.0:8000"]