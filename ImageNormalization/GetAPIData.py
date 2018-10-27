import requests
from APIKey import ReturnAPIKey as key
from ImageNormalization import CoordinateConverter as convert

def getRoadAPIData(latitude, longitude):

    parameters = "points=" + latitude + "," + longitude
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