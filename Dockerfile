FROM python:3.11.9-slim-bullseye

ARG POETRY_VERSION=1.8.2
ARG POETRY_DOWNLOAD=https://install.python-poetry.org
ARG PROJECT_URL=https://github.com/CS3321-Spring-2024/Team_2Project.git
ENV PATH="$PATH:/root/.local/bin"
ARG NASA_API_KEY
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests -y \
        curl \
        git \
        bash

RUN curl -sSL $POETRY_DOWNLOAD | python3 - --version $POETRY_VERSION
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY=/root/.local/bin/poetry
ENV NASA_API_KEY=$NASA_API_KEY
WORKDIR /app
RUN git clone $PROJECT_URL
WORKDIR /app/Team_2Project/team2_proj
RUN git checkout feature19-fixed-dockerfile

RUN poetry install
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["team2_proj/space.py"]
