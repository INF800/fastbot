FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install poetry && poetry install --no-interaction --only main

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]

EXPOSE 8000