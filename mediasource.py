import glob
import os


class MediaSource:
    def __init__(self) -> None:
        path = "photos"
        self.filenames = glob.glob(os.path.join(path, "*"))
        self.index = 0

    def next(self):
        if self.index < len(self.filenames) - 1:
            self.index += 1
        else:
            self.index = 0

    def prev(self):
        if self.index == 0:
            self.index = len(self.filenames) - 1
        else:
            self.index -= 1

    def get(self):
        return self.filenames[self.index]
