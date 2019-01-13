from astropy.io import fits
import numpy as np

def load_fits(img):
  hdulist = fits.open(img)
  data = hdulist[0].data
  ans = np.argmax(data)
  max_pos = np.unravel_index(ans, data.shape)
  return max_pos


'''To solve this problem, you will need to use the Astropy module
to read in the FITS files and to extract the image data, as we've
seen on the two previous slides. Then, to find the brightest pixel
of the image we are looking for the largest value in the 2D array.
The argmax function from numpy provides precisely this
functionality: it searches for the largest value in the array
and returns its position. However, if you've printed out the result
of argmax on its own you would have found that it does not return
a tuple of x and y coordinates but just a single index. Why is that?
This function works on a flattened (or ravelled) array,
i.e. the array gets converted to a 1D array internally
before the maximum is found. To revert this, or to "unravel" the result,
we can call the function unravel_index and pass it the dimension of the
initial data array as second argument.'''
