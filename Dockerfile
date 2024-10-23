# Dockerfile for the Nexus Framework

# Frontend Build
FROM node:14 AS frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Backend Build
FROM python:3.9 AS backend
WORKDIR /app/backend
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .

EXPOSE 5000
CMD ["python", "app.py"]
