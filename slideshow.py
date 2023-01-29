import cv2 as cv


class SlideShow:
    def __init__(self, mediasource, navigation) -> None:
        self.mediasource = mediasource
        self.navigation = navigation

    def next(self) -> None:
        for filename in self.mediasource.next():
            img = cv.imread(filename)
            cv.imshow("Slideshow", img)
            if cv.waitKey(1000) == ord("q"):
                return
