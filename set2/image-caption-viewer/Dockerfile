FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY /app .

# Expose port 5000
EXPOSE 5000

# Run the application
CMD [ "python3", "-m" , "flask", "--debug", "run", "--host=0.0.0.0"]
 