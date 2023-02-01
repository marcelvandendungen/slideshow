import cv2 as cv


class SlideShow:
    def __init__(self, navigation) -> None:
        self.navigation = navigation

    def run(self) -> None:
        try:
            while True:
                filename = self.navigation.get()
                key = self.show(filename)
                self.navigation.next(key)
        except StopIteration:
            pass

    def show(self, filename):
        img = cv.imread(filename)
        cv.imshow("Slideshow", self.resize(img, 750))
        key = cv.waitKey(1000)
        return key

    def resize(self, img, size):
        height, width, _ = img.shape
        if width < height:
            # resize width of portrait photo to fit window
            # scale height to ratio
            height = int(height * size / width)
            width = size
            # resize image
            img = cv.resize(img, (width, height))
            # crop image
            shift = height - size
            img = img[shift // 2 : -shift // 2, :, :]
            return img
        else:
            # resize height of landscape photo to fit window
            # scale width to ratio
            width = int(width * size / height)
            height = size
            shift = width - size
            # resize image
            img = cv.resize(img, (width, height))
            # crop image
            img = img[:, shift // 2 : -shift // 2, :]
            return img
