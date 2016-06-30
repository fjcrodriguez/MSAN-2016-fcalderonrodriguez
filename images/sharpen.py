from filter import *

'''
    laplace compares the strength of the current
    pixel with those surrounding it and returns
    the difference

    :param list
'''


def laplace(list):
    return (list[1] + list[3] + list[5] + list[7]) - (4 * list[0])


'''
   minus subtracts pixel intensities from an image
   with an edge filter from the original image

   :param A (original image)
   :param B (edge filtered image)
'''


def minus(A, B):
    width, height = A.size
    img_copy = A.copy()
    A_matrix = A.load()
    B_matrix = B.load()
    copy_matrix = img_copy.load()

    for x in range(width -1):
        for y in range(height - 1):
            copy_matrix[x, y] = A_matrix[x, y] - B_matrix[x, y]

    return img_copy


img = open(sys.argv)
img.show()
edges = filter(img, laplace)

sharpen = minus(img, edges)

sharpen.show()
