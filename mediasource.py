import glob
import os


class MediaSource:
    def next(self):
        path = "photos"
        filenames = glob.glob(os.path.join(path, "*"))
        for filename in filenames:
            yield filename
