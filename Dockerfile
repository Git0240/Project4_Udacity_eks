# Base image
FROM python:stretch

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
# Copy application files
COPY . .


# Entrypoint to run the app using Gunicorn
ENTRYPOINT ["gunicorn", "-b", ":8080", "app:APP"]
