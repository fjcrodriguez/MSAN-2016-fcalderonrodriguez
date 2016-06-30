from filter import *

'''
    avg returns the average of a list given
    :param list
'''


def avg(list):
    return sum(list) / len(list)

img = open(sys.argv)
img.show()
img = filter(img, avg)
img.show()

