FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the client script
COPY client.py /app/client.py

# Install required Python packages
RUN pip install requests

# Run the Python client with unbuffered output
CMD ["python", "-u", "client.py"]
