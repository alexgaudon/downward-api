FROM python:3.9-slim

WORKDIR /app

# Install uv
RUN pip install uv

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

COPY app.py .
COPY templates/ templates/
COPY static/ static/

EXPOSE 8080

# Use Gunicorn with 4 worker processes
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "app:app"] 