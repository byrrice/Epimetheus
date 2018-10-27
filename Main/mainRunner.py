from CoordsToMapImage.MapImage import getSatImage
from DroneAccessor.DroneRectangle import coordinatesToImageLatLong
from ImageNormalization import GetAPIData as getRoads


def run(centerLat, centerLong, droneImgPath):
    #TODO calculate correct altitude
    toplat, botlat, leftlong, rightlong = coordinatesToImageLatLong(centerLat, centerLong)
    satImgPath = getSatImage(centerLat, centerLong, 18)

    getRoads.doEverything(satImgPath, droneImgPath, botlat, toplat, leftlong, rightlong)

