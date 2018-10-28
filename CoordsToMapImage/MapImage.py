from PIL import Image
from io import BytesIO
import requests

# Coordinates of the center of the image, and zoom based upon FOV and altitude of image
from APIKey import ReturnAPIKey

def getSatImage(coordLat, coordLong, zoom=18):
    URL = "https://maps.googleapis.com/maps/api/staticmap?"
    center = str(coordLat)+','+str(coordLong)
    # Crop out top and bottom 20 pixels to keep image centered
    size = '590x640'
    maptype = 'satellite'
    key = ''
    PARAMS = {'center':center,'zoom':zoom,'size':size,'maptype':maptype,'key':key, 'scale':2}
    
    r = requests.get(url=URL, params=PARAMS)
    img = Image.open(BytesIO(r.content))
    width, height = img.size
    img = img.crop((0,50,width,(height-50)))
    fileName = './Images/img1.png'
    img.save(fileName, 'PNG')

    maptype = 'terrain'
    PARAMS = {'center':center,'zoom':zoom,'size':size,'maptype':maptype,'key':key, 'scale':2}
    
    r = requests.get(url=URL, params=PARAMS)
    img = Image.open(BytesIO(r.content))
    width, height = img.size
    img = img.crop((0,50,width,(height-50)))
    fileName2 = './Images/img2.png'
    img.save(fileName2, 'PNG')


    return fileName, fileName2
