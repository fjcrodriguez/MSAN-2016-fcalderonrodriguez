import sys
from PIL import Image

'''
    flip takes an image and flips it horizontally
    @:param img
'''
def flip(img):

    width, height = img.size
    imgup = img.copy()
    imgup_matrix = imgup.load()
    img_matrix = img.load()

    for row in range(height - 1):
        for col in range(width / 2):
            imgup_matrix[col, row] = img_matrix[width - col - 1, row]
            imgup_matrix[width - col - 1, row] = img_matrix[col, row]

    return imgup

if len(sys.argv) <= 1:
    print "missing image filename"
    sys.exit(1)

filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

img = flip(img)
img.show()
