import requests
from APIKey import ReturnAPIKey as key
from scipy import misc
import numpy as np
from ImageNormalization import Normalizer as norm
from ImageNormalization import GetLatLongFromPix as latLong


def obstructionToLongLat(cameraImageFile, apiImageFile, roadImageFile, latitudeBottom,
        latitudeTop, longitudeLeft, longitudeRight):
    cameraImageArray = norm.imageToArray(cameraImageFile)
    apiImageArray = norm.imageToArray(apiImageFile)

    diffArray = norm.imageDiff(cameraImageArray, apiImageArray)
    roadArray = getRoadPixels(roadImageFile)
    print(np.shape(diffArray))

    diffBinary = np.where(diffArray > 50, 1, 0)
    obstructions = np.where(np.sum(diffBinary, 2) >= 1, 1, 0)
    obstructionsOnRoads = np.where(roadArray + obstructions == 2, 1,0)

    #make new map with obstruction on it.
    newRoadMap = misc.imread(roadImageFile)
    newRoadArray = np.array(newRoadMap)

    newRoadArray[:,:,0] = np.where(obstructionsOnRoads == 1, 255, newRoadArray[:,:,0])
    newRoadArray[:,:,1] = np.where(obstructionsOnRoads == 1, 0, newRoadArray[:,:,1])
    newRoadArray[:,:,2] = np.where(obstructionsOnRoads == 1, 0, newRoadArray[:,:,2])
    misc.imsave('./Images/labeledObstructions.png', newRoadArray)

    pointsToCheck = []
    for i in range(1180):
        for j in range(1180):
            if obstructionsOnRoads[i,j] == 1:
                pointsToCheck.append((latLong.getLatFromPix(i, latitudeBottom, latitudeTop), latLong.getLongFromPix(j, longitudeLeft, longitudeRight)))

    return pointsToCheck

def getRoadPixels(roadImageFile):
    roadImageArray = norm.imageToArray(roadImageFile)
    print(np.shape(roadImageArray))
    flatArray = np.sum(roadImageArray, 2)
    print(flatArray)
    return np.where(flatArray >= 762, 1, 0)

def batchGetRoadAPIData(pointsToCheck):
    roadMap = {}
    if len(pointsToCheck) == 0:
        return roadMap
    if len(pointsToCheck) >= 100:
        for i in range(0, len(pointsToCheck), 100):
            count = min(i+100, len(pointsToCheck))
            placeIDs = getRoadAPIData(pointsToCheck[i:count])
            for j, placeID in enumerate(placeIDs):
                roadName = getPlaceAPIData(placeID)
                if roadName in roadMap:
                    roadMap[roadName].append(pointsToCheck[i+j])
                else:
                    roadMap[roadName] = [pointsToCheck[i+j]]

    leftoverCount = len(pointsToCheck) % 100
    if leftoverCount == 0:
        return roadMap

    placeIDs = getRoadAPIData(pointsToCheck[len(pointsToCheck)-leftoverCount: len(pointsToCheck)])
    i = len(pointsToCheck)-leftoverCount
    for j, placeID in enumerate(placeIDs):
        roadName = getPlaceAPIData(placeID)
        if roadName in roadMap:
            roadMap[roadName].append(pointsToCheck[i + j])
        else:
            roadMap[roadName] = [pointsToCheck[i + j]]

    return roadMap

def getRoadAPIData(points):
    pointStrings = []
    for point in points:
        s = str(point[0]) + "," + str(point[1])
        pointStrings.append(s)
    pointsParam = "|".join(pointStrings)
    parameters = {'points': pointsParam, 'key': key.getAPIKey()}
    url = "https://roads.googleapis.com/v1/nearestRoads?"
    response = requests.get(url, params=parameters)
    data = response.json()
    print(data)
    placeIDs = []
    for snappedPoint in data['snappedPoints']:
        placeIDs.append(snappedPoint["placeId"])

    return placeIDs


def getPlaceAPIData(placeID):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    parameters = {'placeid' : placeID, 'key' : key.getAPIKey()}

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


def doEverything(cameraImageFile, apiImageFile, roadImageFile, latitudeBottom, latitudeTop,
        longitudeLeft, longitudeRight):
    pointsTocheck = obstructionToLongLat(cameraImageFile, apiImageFile, roadImageFile,
                                          latitudeBottom, latitudeTop,
                                          longitudeLeft, longitudeRight)
    roadObstructionMap = batchGetRoadAPIData(pointsTocheck)
    return roadObstructionMap
