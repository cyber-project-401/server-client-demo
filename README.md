# Dockerized TLS Server and Client

This project sets up a simple TLS-enabled server and a client using Docker Compose. The server responds to HTTPS requests with a JSON message, and the client sends periodic requests to the server every 10 seconds.

## How to Run the Project

1. **Generate the TLS Certificate and Key**: (Optional - Only if you want new keys)
   ```bash
   openssl req -new -x509 -days 365 -nodes -out server/cert.pem -keyout server/key.pem -subj "/CN=localhost"
   ```

2. **Build and Start the Docker Containers**:
   ```bash
   docker-compose up --build
   ```

3. **Verify the Server and Client**:
   - Check the logs of the client to see periodic requests:
     ```bash
     docker logs python_client
     ```
   - Check the logs of the server to see requests being handled:
     ```bash
     docker logs tls_server
     ```

4. **Test the Server from Host** (optional):
   You can manually send a request to the server using `curl`:
   ```bash
   curl -k https://localhost:8443
   ```

## Capturing Traffic with `tcpdump`

To monitor the network traffic between the containers, you can use `tcpdump`.

1. **Run `tcpdump` on All Interfaces**:
   ```bash
   sudo tcpdump -i any port 8443
   ```

2. **Save Traffic to a File for Analysis**:
   ```bash
   sudo tcpdump -i any port 8443 -w traffic.pcap
   ```

3. **Analyze Captured Traffic**:
   - View the captured packets:
     ```bash
     tcpdump -r traffic.pcap
     ```

## Important Notes

- **Client Requests Localhost**:
  The client container is designed to request the `server` hostname in the Docker network. However, since the server is running with `localhost` as its certificate Common Name (`CN`), the client is effectively sending requests to `127.0.0.1` within its container. This makes it appear as if the containers are not directly talking to each other.

- **Captured Traffic**:
  When you monitor traffic with `tcpdump`, the packets will appear as if they are originating and terminating within the same container. This is because the client uses `localhost` as the destination for requests.

## Cleaning Up

1. **Stop and Remove the Containers**:
   ```bash
   docker-compose down
   ```

2. **Remove All Containers, Networks, and Images**:
   ```bash
   docker system prune -a
   ```

## Conclusion

This project demonstrates how to set up a simple Dockerized TLS server and client while exploring network monitoring with `tcpdump`. The server handles TLS-secured requests, and the client sends requests periodically. You can use `tcpdump` to capture and analyze the traffic between the client and server containers.
