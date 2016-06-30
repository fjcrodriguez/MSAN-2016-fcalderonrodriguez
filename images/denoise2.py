from filter import *


'''
    the median of a list given
    :param list
'''


def median(data):
    sorted_list = sorted(data)
    idx_len = len(sorted_list) - 1  # length of list in zero index
    if len(sorted_list) % 2 == 0:
        first_num = sorted_list[idx_len/2]
        second_num = sorted_list[idx_len/2 + 1]
        return (first_num + second_num)/2
    else:
        return sorted_list[idx_len/2]


img = open(sys.argv)
img.show()
img = filter(img, median)
img.show()
