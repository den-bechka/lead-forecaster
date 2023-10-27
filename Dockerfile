# Using the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
RUN mkdir -p /app
WORKDIR /app

ENV PYTHONPATH=/app

# Copy the dependency files into the working directory
COPY ./requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copying the project source code into the working directory
COPY ./app /app

# Declare the port on which the application will run
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "8000"]