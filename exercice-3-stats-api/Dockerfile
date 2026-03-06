#bulder
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip wheel --wheel-dir=/wheels -r requirements.txt
#runtime
FROM python:3.12-alpine AS runtime
WORKDIR /app
COPY --from=builder /wheels /wheels
COPY requirements.txt .
RUN pip install --no-cache-dir --find-links=/wheels -r requirements.txt
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]