# from screeninfo import get_monitors

from mediasource import MediaSource
from navigation import Navigation
from slideshow import SlideShow

# for m in get_monitors():
#     print(str(m))


def main():
    navigation = Navigation()
    mediasource = MediaSource()
    slideshow = SlideShow(mediasource, navigation)

    while slideshow:
        slideshow.next()


if __name__ == "__main__":
    main()
