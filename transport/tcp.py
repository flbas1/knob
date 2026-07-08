import json
import socket
from typing import Any


class TcpTransport:

    def __init__(self, host: str = "127.0.0.1", port: int = 5000):
        self.host = host
        self.port = port
        self.socket: socket.socket | None = None

    def connect(self):
        self.socket = socket.create_connection(
            (self.host, self.port)
        )

    def send(self, payload: Any):
        message = json.dumps(payload) + "\n"

        if self.socket is None:
            raise RuntimeError("Transport is not connected")

        self.socket.sendall(
            message.encode("utf-8")
        )

    def close(self):
        if self.socket:
            self.socket.close()
            self.socket = None