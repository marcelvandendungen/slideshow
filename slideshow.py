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
        cv.imshow("Slideshow", img)
        key = cv.waitKey(1000)
        return key
