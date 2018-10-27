import requests
from APIKey import ReturnAPIKey as key
import numpy as np
from ImageNormalization import Normalizer as norm
from ImageNormalization import GetLatLongFromPix as latLong


def obstructionToLongLat(cameraImageFile, apiImageFile, latitudeBottom,
        latitudeTop, longitudeLeft, longitudeRight):
    cameraImageArray = norm.imageToArray(cameraImageFile)
    apiImageArray = norm.imageToArray(apiImageFile)

    diffArray = norm.imageDiff(cameraImageArray, apiImageArray)
    convertedArray = []

    for i in range(0, 1080):
        for j in range(0, 1080):
            if np.absolute(diffArray[i][j]) > 50:
                convertedArray.append(
                        tuple((latLong.getLatFromPix(i, latitudeBottom,
                                                     latitudeTop),
                               latLong.getLongFromPix(j, longitudeLeft,
                                                      longitudeRight))))

    return convertedArray


def getRoadAPIData(latLong):
    parameters = "points=" + latLong[0] + "," + latLong[1]
    apikey = "&key=" + key.getAPIKey()
    url = "https://roads.googleapis.com/v1/nearestRoads?" + parameters + apikey

    response = requests.get(url)
    data = response.json

    placeID = data["placeId"]
    return placeID


def getPlaceAPIData(placeIDArray):
    apikey = "&key=" + key.getAPIKey()
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


def doEverything(cameraImageFile, apiImageFile, latitudeBottom, latitudeTop,
        longitudeLeft, longitudeRight):
    convertedArray = obstructionToLongLat(cameraImageFile, apiImageFile,
                                          latitudeBottom, latitudeTop,
                                          longitudeLeft, longitudeRight)
    roadList = getRoadList(convertedArray)

    return roadList
