# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install the Python dependencies
RUN pip install requests

# Copy the Python script into the container
COPY spider.py .

# Set the command to run the Python spider
CMD ["python", "spider.py"]