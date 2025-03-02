import os

# Enable TLS session key logging
os.environ["SSLKEYLOGFILE"] = "/tmp/sslkey.log"

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(message="Hello, TLS-secured world!")

if __name__ == "__main__":
    cert_path = os.path.join(os.path.dirname(__file__), "cert.pem")
    key_path = os.path.join(os.path.dirname(__file__), "key.pem")
    app.run(host="0.0.0.0", port=8443, ssl_context=(cert_path, key_path))
