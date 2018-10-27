from scipy import misc
import numpy as np


def imageToArray(filename):
    mapScreenShot = misc.imread(filename)
    mapScreenShotArray = np.array(mapScreenShot)

    return mapScreenShotArray


def imageDiff(cameraImageArray, apiImageArray):
    diffArray = np.subtract(cameraImageArray, apiImageArray)
    return diffArray



