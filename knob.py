from transport.tcp import TcpTransport
from runtime.protocol import Payload


def main():

    device = TcpTransport()

    device.connect()

    payload: Payload = {
        # "type": "Payload",
        "screen": "launcher",
        "selected": 1
    }

    device.send(payload)

    device.close()


if __name__ == "__main__":
    main()


# import json
# import socket
# from typing import TypedDict

# sock = socket.create_connection(("127.0.0.1", 5000))

# class Payload(TypedDict):
#     screen: str
#     selected: int

# payload: Payload = {
#     "screen": "launcher",
#     "selected": 1
# }

# sock.sendall((json.dumps(payload) + "\n").encode("utf-8"))



# from plugins.scroll.plugin import Plugin


# def main():
#     print("Knob Runtime 0.1")

#     plugin = Plugin()

#     while True:
#         command = input("Rotate (+/-): ")

#         if command == "q":
#             break

#         try:
#             amount = int(command)
#             plugin.on_rotate(amount)
#         except ValueError:
#             print("Enter an integer or q.")


# if __name__ == "__main__":
#     main()