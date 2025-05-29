# Use an official lightweight Python image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code into the container
COPY . .

# Expose port 5000 to the host
EXPOSE 5000

# Command to run the app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "flaskapp:app"]
