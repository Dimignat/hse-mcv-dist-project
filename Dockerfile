FROM python:3.9-slim

WORKDIR /app
COPY . /app/

RUN python3 -m pip install poetry \
	&& python3 -m poetry config virtualenvs.in-project true \
	&& python3 -m poetry install --no-root

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT [".venv/bin/python", "-m", "streamlit", "run", "streamlit_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]

