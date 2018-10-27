from CoordsToMapImage.MapImage import getSatImage
from DroneAccessor.DroneRectangle import coordinatesToImageLatLong
from ImageNormalization.Normalizer import imageToArray


def run(centerLat, centerLong, droneImgPath):
    #TODO calculate correct altitude
    toplat, botlat, leftlong, rightlong = coordinatesToImageLatLong(centerLat, centerLong)
    satImgPath = getSatImage(centerLat, centerLong, 18)
    satImgArray = imageToArray(satImgPath)
    droneImgArray = imageToArray(droneImgPath)

