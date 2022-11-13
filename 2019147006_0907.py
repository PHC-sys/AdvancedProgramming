from haversine import haversine
from geographiclib.geodesic import Geodesic

lat1 = 37.566398
lon1 = 126.938803
lat2 = 37.586830986
lon2 = 127.025999896

#DD Coordinates of Yonsei Univ. & Korea Univ.
YSU = (lat1, lon1)
KRU = (lat2, lon2)

dist = haversine(YSU, KRU, unit='m')
half_dist = dist/2

#Define the ellipsoid
geod = Geodesic.WGS84

#Solve the Inverse problem for calculation of Azimuth
inv = geod.Inverse(YSU[0], YSU[1], KRU[0], KRU[1])
azi1 = inv['azi1']

#Solve the Direct problem
dir = geod.Direct(YSU[0], YSU[1], azi1, half_dist)
MidPoint = (dir['lat2'], dir['lon2'])

print("Distance:", dist)
print("MidPoint:", MidPoint)
