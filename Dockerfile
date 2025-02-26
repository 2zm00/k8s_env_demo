# Dockerfile 생성
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# .env 파일은 복사하지 않음!

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]