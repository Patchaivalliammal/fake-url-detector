# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
RUN pip install -r src/requirements.txt

# Train a fresh valid model inside the container (avoids corrupted files)
RUN python src/train_model.py

EXPOSE 5000
CMD ["python", "src/app.py"]
