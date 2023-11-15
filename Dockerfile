FROM python:3.10.12

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000
ENV PORT 8000

CMD ["/bin/bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 2>&1 | tee /var/log/logs.txt"]