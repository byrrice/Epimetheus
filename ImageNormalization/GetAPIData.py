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
    print(np.shape(diffArray))
    for i in range(0, 1240):
        for j in range(0, 1240):
            if abs(diffArray[i,j,0]) > 50 or abs(diffArray[i,j,1]) > 50 or abs(diffArray[i,j,2]) > 50:
                convertedArray.append(
                        tuple((latLong.getLatFromPix(i, latitudeBottom,
                                                     latitudeTop),
                               latLong.getLongFromPix(j, longitudeLeft,
                                                      longitudeRight))))

    return convertedArray


def getRoadAPIData(latLong):
    parameters = {'points': str(round(latLong[0], 3)) + "," + str(round(latLong[1],3)), 'key': key.getAPIKey()}
    url = "https://roads.googleapis.com/v1/nearestRoads?"
    response = requests.get(url, params=parameters)
    data = response.json()
    # print(data)
    placeID = data['snappedPoints'][0]["placeId"]
    return placeID


def getPlaceAPIData(placeIDArray):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    parameters = {'placeid' : placeIDArray, 'key' : key.getAPIKey()}

    response = requests.get(url, parameters)
    data = response.json()
    # print(data)
    roadName = data["result"]["formatted_address"]
    return roadName


def getRoadList(convertedArray):
    roadList = []

    for i in range(0, len(convertedArray)):
        roadList.append(getPlaceAPIData(getRoadAPIData(convertedArray[i])))

    return roadList


def doEverything(cameraImageFile, apiImageFile, latitudeBottom, latitudeTop,
        longitudeLeft, longitudeRight):
    convertedArray = obstructionToLongLat(cameraImageFile, apiImageFile,
                                          latitudeBottom, latitudeTop,
                                          longitudeLeft, longitudeRight)
    roadList = getRoadList(convertedArray)

    return roadList
