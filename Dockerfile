FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/
COPY frontend/ ./frontend/

# for deployment (use other library for flask and front)
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-5000} --chdir backend app:app"]
