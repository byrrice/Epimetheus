import numpy as np


def convertPixelToWorld(pixelCoordX, pixelCoordY, zoomLevel):
    worldCoordX = np.multiply(pixelCoordX, np.power(2, -zoomLevel))
    worldCoordY = np.multiply(pixelCoordY, np.power(2, -zoomLevel))

    return [worldCoordX, worldCoordY]


def convertWorldToLongLat(worldCoordArray):
    longitude = np.subtract(
            np.multiply((np.divide(worldCoordArray[0], 256)), 360), 180)

    insideFunc = np.subtract(np.pi, (
        np.divide(np.multiply(np.multiply(2, np.pi), worldCoordArray[1]), 256)))

    latitude = np.multiply(np.divide(180, np.pi)), np.atan(
            np.multiply(0.5,
                        np.subtract(np.exp(insideFunc), np.exp(-insideFunc))))

    return [latitude, longitude]
