FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all bot files
COPY . .

# Default command
CMD ["python3", "bot.py"]
