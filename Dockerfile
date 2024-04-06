FROM python:3.11 AS builder

WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN python -m pip install --no-cache-dir poetry==1.8.2 \
    && poetry config virtualenvs.in-project true \
    && poetry install --without dev,test --no-interaction --no-ansi

FROM python:3.11-slim

WORKDIR /app
COPY --from=builder /app /app
COPY web_app.py ./
COPY static ./
COPY templates ./

CMD ["/app/.venv/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]