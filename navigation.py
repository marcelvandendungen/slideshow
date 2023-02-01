class Navigator:
    def __init__(self, source) -> None:
        self.source = source

    def get(self):
        return self.source.get()

    def next(self, key):
        pass


class KeyboardNavigator(Navigator):
    def next(self, key):
        if key & 0xFF == ord("n"):
            self.source.next()
        elif key & 0xFF == ord("p"):
            self.source.prev()
        elif key & 0xFF == ord("q"):
            raise StopIteration()


class HttpNavigator(Navigator):
    pass
