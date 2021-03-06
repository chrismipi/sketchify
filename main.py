import numpy as np
import imageio
import scipy.ndimage
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


def dodge(front, back):
    result = front * 255 / (255 - back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')


def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


if __name__ == '__main__':
    img = "http://static.cricinfo.com/db/PICTURES/CMS/263600/263697.20.jpg"

    s = imageio.imread(img)
    g = grayscale(s)
    i = 255 - g

    b = scipy.ndimage.filters.gaussian_filter(i, sigma=10)
    r = dodge(b, g)

    plt.imshow(r, cmap="gray")

    plt.savefig('~/to.png', img)  # save the figure to file
    plt.close(r)
