FROM python:3.12.4-slim-bookworm

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

CMD ["./entrypoint.sh"]