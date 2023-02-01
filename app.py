from mediasource import MediaSource
from navigation import KeyboardNavigator
from slideshow import SlideShow

mediasource = MediaSource()
navigator = KeyboardNavigator(mediasource)


def main():
    slideshow = SlideShow(navigator)
    slideshow.run()


if __name__ == "__main__":
    main()
