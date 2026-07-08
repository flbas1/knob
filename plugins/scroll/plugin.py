from runtime.providers.scroll import ScrollProvider


class Plugin:
    def __init__(self):
        self.scroll = ScrollProvider()

    def on_rotate(self, amount: int):
        self.scroll.scroll(amount)