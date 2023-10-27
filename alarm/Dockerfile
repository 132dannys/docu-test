FROM python:3.11.4-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    build-essential \
    python3-dev \
    libpq-dev \
    tzdata \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

RUN pip install --no-cache -U pip setuptools poetry==1.4.0 \
    && rm -rf /root/.cache/pip

COPY . .

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-cache --no-ansi --no-interaction --only main \
    && poetry cache clear pypi --all

CMD ["python", "memory_alarm.py"]