import sys
from PIL import Image


'''
    region3x3 gets the pixels around x, y
    and returns a list of all 8 surrounding pixels
    including the center pixel at x, y
    :param img
    :param x, y
'''


def region3x3(img, x ,y):
    center = get_pixel(img, x, y)
    N = int(get_pixel(img, x, y - 1))
    NE = int(get_pixel(img, x + 1, y -1))
    E = int(get_pixel(img, x + 1, y))
    SE = int(get_pixel(img, x + 1, y + 1))
    S = int(get_pixel(img, x, y + 1))
    SW = int(get_pixel(img, x - 1, y + 1))
    W = int(get_pixel(img, x - 1, y))
    NW = int(get_pixel(img, x - 1, y - 1))
    return [center, N, NE, E, SE, S, SW, W, NE, NW]


'''
    get_pixel returns the pixel at x and y
    :param img
    :param x, y
'''


def get_pixel(img, x, y):
    width, height = img.size
    if x < 0:
        x = 0
    elif x >= width:
        x = width - 1

    if y < 0:
        y = 0
    elif y >= height:
        y = height - 1

    return img.load()[x, y]




'''
    opens a picture file provided
    :param argv
'''


def open(argv):
    if len(argv) <= 1:
        print "mising image filename"
        sys.exit(1)
    img = Image.open(argv[1])
    img = img.convert("L")
    return img




'''
    applies filter to image provided
    filter behavior is determined by
    the function f that is provided

    :param imh
    :param f
'''


def filter(img, f):
    width, height = img.size
    img_copy = img.copy()
    pixels = img_copy.load()

    for x in range(width - 1):
        for y in range(height - 1):
            r = region3x3(img, x, y)
            pixels[x, y] = f(r)

    return img_copy

