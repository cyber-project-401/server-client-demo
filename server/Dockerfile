FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy server code and TLS certificates
COPY server.py /app/server.py
COPY cert.pem /app/cert.pem
COPY key.pem /app/key.pem

# Install Flask
RUN pip install flask

# Run the server
CMD ["python", "server.py"]
