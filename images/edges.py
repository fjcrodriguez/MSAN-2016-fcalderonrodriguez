from filter import *


def laplace(list):
    return (list[1] + list[3] + list[5] + list[7]) - (4 * list[0])

img = open(sys.argv)
img.show()
edges = filter(img, laplace)
edges.show()

