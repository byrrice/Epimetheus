import math

def coordinatesToImageLatLong(centerLat, centerLong, zoom=18):
    #returns toplat, botlat, leftlong, rightlong
    metersPerPx = 156543.03392 * math.cos(centerLat * math.pi / 180) / math.pow(2, zoom)
    lats = getLats(centerLat, metersPerPx)
    longs = getLongs(centerLat, centerLong, metersPerPx)
    return lats[1], lats[0], longs[0], longs[1]

def getLongs(centerLat, centerLong, metersFrom):
    longdif = metersFrom * longPerMeter(centerLat)
    return centerLong - longdif, centerLong+longdif

def getLats(centerLat, metersFrom):
    latitudeMetersRation = 0.000009
    return centerLat - metersFrom * latitudeMetersRation, centerLat + metersFrom * latitudeMetersRation


def longPerMeter(latTheta):
    r_earth = 6.378137e6
    return (2 * math.pi / 360) * r_earth * 1/math.cos(latTheta)

def LatDegreesPerMeter(latTheta):
    111111