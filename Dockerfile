FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN chmod +x app.py

CMD ["./app.py"] 