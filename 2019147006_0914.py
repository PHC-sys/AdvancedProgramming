from haversine import haversine
from geographiclib.geodesic import Geodesic

#this is the function from first assignment(0907)
#Fucntion for Calculating Midpoint
def CalMidpoint(lat1,lon1,lat2,lon2):
    FirstPoint = (lat1, lon1)
    SecondPoint = (lat2, lon2)

    dist = haversine(FirstPoint, SecondPoint, unit='m')
    half_dist = dist / 2

    # Define the ellipsoid
    geod = Geodesic.WGS84

    # Solve the Inverse problem for calculation of Azimuth
    inv = geod.Inverse(FirstPoint[0], FirstPoint[1], SecondPoint[0], SecondPoint[1])
    azi1 = inv['azi1']

    # Solve the Direct problem
    dir = geod.Direct(FirstPoint[0], FirstPoint[1], azi1, half_dist)
    MidPoint = (dir['lat2'], dir['lon2'])

    return MidPoint

#Location chosen: Seoul
lat11 = 37.5595
lon11 = 126.7733
lat12 = 37.5595
lon12 = 127.182

lat21 = 37.4974
lon21 = 126.8147
lat22 = 37.4974
lon22 = 127.1606

MidPoint1 = CalMidpoint(lat11, lon11, lat12, lon12)
MidPoint2 = CalMidpoint(lat21, lon21, lat22, lon22)

print("MidPoint1:", MidPoint1)
print("MidPoint2:", MidPoint2)

print("Conclusion: According to the data of Seoul, government should invest for the hospitals and schools to the east Seoul.")
