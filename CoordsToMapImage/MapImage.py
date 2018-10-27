from PIL import Image
from io import BytesIO
import requests
import apiKey

# Coordinates of the center of the image, and zoom based upon FOV and altitude of image
def getSatImage(coordLat, coordLong, zoom=18):
    URL = "https://maps.googleapis.com/maps/api/staticmap?"
    center = str(coordLat)+','+str(coordLong)
    # Crop out top and bottom 20 pixels to keep image centered
    size = '1080x1120'
    maptype = 'satellite'

    key = apiKey.getKey()
    
    PARAMS = {'center':center,'zoom':zoom,'size':size,'maptype':maptype,'key':key}
    
    r = requests.get(url=URL, params=PARAMS)
    img = Image.open(BytesIO(r.content))
    width, height = img.size
    img = img.crop((0,20,width,(height-20)))
    # img.show()
    return img

if __name__ == "__main__":
    img = getSatImage(40.714728,-73.998672)
    img.show()
