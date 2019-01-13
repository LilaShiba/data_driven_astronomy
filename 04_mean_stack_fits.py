from astropy.io import fits
import numpy as np

# Write your mean_fits function here:
def mean_fits(files):
  n = len(files)
  hdulist = fits.open(files[0])
  data = hdulist[0].data
  # By calling hdulist.close() we free up the memory this file has taken up
  # while we were working with it.
  hdulist.close()

  for x in range(1, n):
    hdulist = fits.open(files[x])
    data += hdulist[0].data
    hdulist.close()

  mean = data/n
  return mean

mean_fits(fits_00)
