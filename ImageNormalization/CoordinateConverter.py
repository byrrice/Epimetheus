import numpy as np

#legacy function
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
    width = 1180
    longitudeDiff = np.subtract(longitudeRight, longitudeLeft)
    ratio = np.divide(longitudeDiff, width)

    return ratio

def rowRatioFinder(latitudeBottom, latitudeTop):
    height = 1180
    latitudeDiff = np.subtract(latitudeTop, latitudeBottom)
    ratio = np.divide(latitudeDiff, height)

    return ratio



