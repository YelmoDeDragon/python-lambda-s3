# Use Python 3.9.6 slim as base image
FROM python:3.9.6-slim-buster

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies in a virtual environment
RUN python -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Use venv's python to run the script
# CMD ["/app/venv/bin/python", "your_script.py"]
