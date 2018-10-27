import numpy as np
from ImageNormalization import CoordinateConverter as converter


def getLatFromPix(pixRowIndex, latitudeBottom, latitudeTop):
    latitudeOfPix = latitudeBottom + (
                pixRowIndex * converter.rowRatioFinder(latitudeBottom,
                                                       latitudeTop))

    return latitudeOfPix

def getLongFromPix(pixColIndex, longitudeLeft, longitudeRight):
    longitudeOfPix = longitudeLeft + (
            pixColIndex * converter.rowRatioFinder(longitudeLeft,
                                                       longitudeRight))

    return longitudeOfPix


