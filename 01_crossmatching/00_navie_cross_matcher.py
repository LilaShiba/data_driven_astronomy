# Equatorial Coordinate System
# https://www.youtube.com/watch?v=WvXTUcYVXzI
# https://www.youtube.com/watch?v=RbPnXF-eeTU
# Right ascension
# HMS to Degrees
# print(15*(23 + 12/60 + 6/(60*60)))

# Declination
# DMS
# print(73 + 21/60 + 14.4/(60*60))
# or with negative angles
# print(-1*(5 + 31/60 + 12/(60*60)))

import numpy as np

def hms2dec(h,m,s):
    # convert right ascension from HMS to degrees
    return (15*(h + m/60 + s/(60*60)))

def dms2dec(d,m,s):
    # convert declination from DMS to decimal degrees
    if d < 0:
        d = d * -1
        return (-1*(d + m/60 + s/(60*60)))
    else:
        return(d + m/60 + s/(60*60))

'''To crossmatch two catalogues we need to compare the
    angular distance between objects on the celestial sphere.
    People loosely call this a "distance", but technically its
    an angular distance: the projected angle between objects as
    seen from Earth.'''

# use https://en.wikipedia.org/wiki/Haversine_formula
def angular_dist(RA1, dec1, RA2, dec2):
  # Convert to radians
  r1 = np.radians(RA1)
  d1 = np.radians(dec1)
  r2 = np.radians(RA2)
  d2 = np.radians(dec2)

  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2

  angle = 2*np.arcsin(np.sqrt(a + b))

  # Convert back to degrees
  return np.degrees(angle)
