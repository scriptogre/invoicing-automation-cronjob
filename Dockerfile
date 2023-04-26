# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Show logs in real time
ENV PYTHONUNBUFFERED=1

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port (Change this to the port your application is running on)
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
