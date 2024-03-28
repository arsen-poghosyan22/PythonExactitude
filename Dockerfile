# Use the official Python image as a base image
FROM python:3.9-slim

# Copy the content of the local src directory to the working directory
COPY ./app /app

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that FastAPI runs on
EXPOSE 8000

# Command to run the FastAPI application with host and port configuration
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
