FROM python:3.12
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry==2.1.1 && poetry install --no-dev
COPY . .
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]
