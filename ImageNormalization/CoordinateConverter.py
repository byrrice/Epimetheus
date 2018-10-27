import numpy as np


def converCoords(pixelCoord, zoomLevel):
    worldCoord = np.multiply(pixelCoord, np.power(2, -zoomLevel))
    return worldCoord
