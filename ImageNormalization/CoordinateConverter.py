import numpy as np

def convertWorldToLongLat(worldCoordArray):
    longitude = np.subtract(
            np.multiply((np.divide(worldCoordArray[0], 256)), 360), 180)

    insideFunc = np.subtract(np.pi, (
        np.divide(np.multiply(np.multiply(2, np.pi), worldCoordArray[1]), 256)))

    latitude = np.multiply(np.divide(180, np.pi)), np.atan(
            np.multiply(0.5,
                        np.subtract(np.exp(insideFunc), np.exp(-insideFunc))))

    return [latitude, longitude]

def columnRatioFinder(longitudeLeft, longitudeRight):
    width = 1080
    longitudeDiff = np.subtract(longitudeRight, longitudeLeft)
    ratio = np.divide(longitudeDiff, width)

    return ratio

def rowRatioFinder(latitudeTop, latitudeBottom):
    height = 1080
    latitudeDiff = np.subtract(latitudeTop, latitudeBottom)
    ratio = np.divide(latitudeDiff, height)

    return ratio



