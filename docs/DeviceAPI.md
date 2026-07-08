Device

VirtualDevice

SerialDevice

PhoneDevice

HIDDevice

connect()

disconnect()

read_events()

render(view)


class Device:
    def connect(self):
        pass

    def disconnect(self):
        pass

    def send(self, payload):
        pass

    def receive(self):
        pass
        