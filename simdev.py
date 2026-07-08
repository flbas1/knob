#!/usr/bin/env python3
"""
simdev.py

Simple Knob simulator.

Acts like a device by listening on localhost:5000.
Any JSON received is printed to the console.
"""

import json
import socket

HOST = "127.0.0.1"
PORT = 5000


def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)

        print(f"SimDevice listening on {HOST}:{PORT}")
        print("Waiting for runtime...")

        conn, addr = server.accept()

        print(f"Connected from {addr}")

        with conn:

            buffer = ""

            while True:

                data = conn.recv(4096)

                if not data:
                    break

                buffer += data.decode("utf-8")

                #
                # Messages are newline delimited.
                #
                while "\n" in buffer:

                    line, buffer = buffer.split("\n", 1)

                    if not line.strip():
                        continue

                    try:

                        payload = json.loads(line)

                        print()
                        print("========== DEVICE ==========")
                        print(json.dumps(payload, indent=4))
                        print("============================")
                        print()

                    except json.JSONDecodeError as ex:

                        print("Invalid JSON")
                        print(ex)

        print("Runtime disconnected.")


if __name__ == "__main__":
    main()