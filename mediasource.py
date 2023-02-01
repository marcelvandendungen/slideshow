import glob
import os


class MediaSource:
    def __init__(self) -> None:
        path = "photos"
        self.filenames = glob.glob(os.path.join(path, "*"))
        self.index = 0

    def next(self):
        self.index += 1

    def prev(self):
        self.index -= 1

    def get(self):
        return self.filenames[self.index]
