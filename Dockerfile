# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application using Gunicorn, a production-ready WSGI HTTP server.
# This command starts Gunicorn with 4 worker processes, binding to all interfaces
# on port 5000, and running the 'app' object from 'app.py'.
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]
