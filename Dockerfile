FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install ffmpeg libsm6 libxext6 python3 python3-pip -y --no-install-recommends  \
    && apt-get clean

WORKDIR /app
COPY . /app/

RUN python3 -m pip install poetry \
	&& python3 -m poetry config virtualenvs.in-project true \
	&& python3 -m poetry install --no-root \
    && .venv/bin/python -m pip install tensorflow==2.11.0 --ignore-installed

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT [".venv/bin/python", "-m", "streamlit", "run", "streamlit_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
