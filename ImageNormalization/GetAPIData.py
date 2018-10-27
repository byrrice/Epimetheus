import requests
from APIKey import ReturnAPIKey as key
from ImageNormalization import CoordinateConverter as convert
from ImageNormalization import Normalizer as obstructionArray
from ImageNormalization import GetLatLongFromPix as latLong


def obstructionToLongLat():
    diffArray = obstructionArray.imageDiff()
    convertedArray = []

    for i in range(0, 1080):
        for j in range(0, 1080):
            if diffArray[i][j] > 0:
                convertedArray.append(
                        tuple((latLong.getLatFromPix(i, latitudeBottom,
                                                     latitudeTop),
                               latLong.getLongFromPix(j, longitudeLeft,
                                                      longitudeRight))))

    return convertedArray


def getRoadAPIData(latLong):
    parameters = "points=" + latLong[0] + "," + latLong[1]
    apikey = "&key=" + key.throwAPIKey()
    url = "https://roads.googleapis.com/v1/nearestRoads?" + parameters + apikey

    response = requests.get(url)
    data = response.json

    placeID = data["placeId"]
    return placeID


def getPlaceAPIData(placeIDArray):
    apikey = "&key=" + key.throwAPIKey()
    parameters = "json?placeID=" + placeIDArray
    url = "https://maps.googleapis.com/maps/api/place/details/"

    response = requests.get(url)
    data = response.json

    roadName = data["result"]["formatted_address"]
    return roadName


def getRoadList(convertedArray):
    roadList = []

    for i in range(0, convertedArray.length):
        roadList.append(getPlaceAPIData(getRoadAPIData(convertedArray[i])))

    return roadList
