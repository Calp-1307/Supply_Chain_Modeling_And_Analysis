"""
Great Circle distance @author: carlo
"""
import numpy as np

coordinate={}
coordinate['Miami']=[25.926420892828713, -80.1979474935445]
coordinate['Raleigh']=[35.95967154096654, -79.12385971809748]

def greatCircleDistance(point1,point2,circuityFactor=1):   
    lat1=point1[0]*2*np.pi/360                   # Changing the latitud from Degrees to radians                 
    lat2=point2[0]*2*np.pi/360
    deltaLatitud=(point1[0]-point2[0])/2         # Changing the latitud from Degrees to radians
    deltaLongitud=(point1[1]-point2[1])/2        # Changing the latitud from Degrees to radians
    deltaLatitudRad=deltaLatitud*2*np.pi/360     # Changing the latitud from Degrees to radians
    deltaLongitudRad=deltaLongitud*2*np.pi/360   # Changing the latitud from Degrees to radians
    r=3958.8                                     # Earth Radius
    gcd_1=np.sqrt((np.sin(deltaLatitudRad)**2)+np.cos(lat1)*np.cos(lat2)*(np.sin(deltaLongitudRad)**2))
    gcd=round(2*r*np.arcsin(gcd_1),2)*circuityFactor
    return gcd
    
    
dist=greatCircleDistance(coordinate['Miami'],coordinate['Raleigh'],1.2)    
    
print(dist)    
