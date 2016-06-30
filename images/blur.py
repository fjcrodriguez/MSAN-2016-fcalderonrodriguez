import sys
from PIL import Image

'''
    blur takes an average of the
    surrounding pixels and sets each
    pixel to that average to blur
    the entire image
    :param img
'''


def blur(img):

    width, height = img.size
    img_copy = img.copy()
    pixels = img_copy.load()

    for x in range(width - 1):
        for y in range(height - 1):
            r = region3x3(img, x, y)
            pixels[x, y] = avg(r)

    return img_copy



'''
    avg returns the average of a list given
    :param list
'''


def avg(list):
    return sum(list) / len(list)


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




if len(sys.argv) <= 1:
    print "missing image filename"
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

img = blur(img)
img.show()
