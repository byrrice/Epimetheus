from CoordsToMapImage.MapImage import getSatImage
from DroneAccessor.DroneRectangle import coordinatesToImageLatLong
from ImageNormalization import GetAPIData as getRoads


def run(centerLat, centerLong, droneImgPath):
    #TODO calculate correct altitude
    toplat, botlat, leftlong, rightlong = coordinatesToImageLatLong(centerLat, centerLong)
    satImgPath, roadImgPath = getSatImage(centerLat, centerLong, 18)

    return getRoads.doEverything(droneImgPath, satImgPath, roadImgPath, botlat, toplat, leftlong, rightlong)

if __name__ == "__main__":
    # print(run(40.0065128,-83.03053321237,'./Images/testImage1.png'))
    # print("Done 1")
    # input()
    # print(run(39.9959124,-82.9981831,'./Images/testImage2.png'))
    # print("Done 2")
    # input()
    print(run(39.8582479,-83.2199184,'./Images/testImage3.png'))
    # print("Done 3")
    # input()
    # print(run(39.8512809,-83.1647455,'./Images/testImage4.png'))
