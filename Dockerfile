# Use a lightweight base image
FROM python:3.11-slim-bookworm

# Update system packages to fix vulnerabilities and remove unnecessary files
RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variable for Flask to find your app factory
ENV FLASK_APP=heyapp:create_app
# Or development, depending on your build stage
ENV FLASK_CONFIG=production 

# Expose the port your Flask app will run on
EXPOSE 8080

ENV GUNICORN_CMD_ARGS="--bind 0.0.0.0:8080 --log-level debug --workers 4"
# Arguments picked up from ENV
CMD ["gunicorn", "heyapp:create_app()"] 
