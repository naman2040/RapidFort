# Use an official Python runtime as the base image
FROM python:3.8.8

# Set the working directory
WORKDIR /app

# Install required packages
COPY . /app
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the Flask app
CMD python ./API.py
