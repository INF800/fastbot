FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --only main

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]

EXPOSE 80