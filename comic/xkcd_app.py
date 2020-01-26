import xkcd

def getRandomXkcdImage():
    try:
        randomComic = xkcd.getRandomComic()
        print(randomComic)
        return [randomComic.getTitle(), randomComic.getAltText(), randomComic.getImageLink()]
    except Exception as e:
        return None
    