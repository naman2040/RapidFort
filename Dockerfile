# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory
WORKDIR /app

# Install required packages
COPY . /app
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
