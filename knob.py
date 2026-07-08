from plugins.scroll.plugin import Plugin


def main():
    print("Knob Runtime 0.1")

    plugin = Plugin()

    while True:
        command = input("Rotate (+/-): ")

        if command == "q":
            break

        try:
            amount = int(command)
            plugin.on_rotate(amount)
        except ValueError:
            print("Enter an integer or q.")


if __name__ == "__main__":
    main()