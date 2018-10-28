from CoordsToMapImage.MapImage import getSatImage
from DroneAccessor.DroneRectangle import coordinatesToImageLatLong
from ImageNormalization import GetAPIData as getRoads


def run(centerLat, centerLong, droneImgPath):
    #TODO calculate correct altitude
    toplat, botlat, leftlong, rightlong = coordinatesToImageLatLong(centerLat, centerLong)
    satImgPath, roadImgPath = getSatImage(centerLat, centerLong, 18)

    return getRoads.doEverything(droneImgPath, satImgPath, roadImgPath, botlat, toplat, leftlong, rightlong)

if __name__ == "__main__":
    print(run(40.0065128,-83.03053321237,'./Images/img.png'))
