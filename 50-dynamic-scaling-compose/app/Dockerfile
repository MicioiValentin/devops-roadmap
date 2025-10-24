FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=5s --timeout=2s --retries=10 CMD python -c "import socket; import sys; s=socket.sockt(); s.settimeout(1); s.connect(('127.0.0.1',8000)); s.close() or sys.exit(0)"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]