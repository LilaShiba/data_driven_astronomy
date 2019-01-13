'''One of the most widely used formats for astronomical images
is the Flexible Image Transport System. In a FITS file, the image
is stored in a numerical array, which we can load into a NumPy array.'''

'''FITS files are a standard format and astronomers have developed
many libraries (in many programming languages) that can read and write
FITS files. We're going to use the Astropy module.'''

# The following code shows how we can open a FITS file
# and print out its header information:

from astropy.io import fits
hdulist = fits.open('image0.fits')
hdulist.info()


'''Opening a FITS file in Astropy returns a HDU (Header/Data Unit) list.
Each HDU stores headers and (optionally) image data. The header contains metadata
about the HDU object, e.g. its dimensions and data type. Every HDU can contain
image data. The first HDU is called the primary HDU. If we want to access individual
HDUs, we can index the HDU list object returned by fits.open. The image data can be
accessed using the data attribute:'''

data = hdulist[0].data
print(data.shape)


''' You often want to visualise the image data stored in FITS files.
We can do this using the plotting library matplotlib.
This example creates a 2D plot from the previous FITS image:'''


import matplotlib.pyplot as plt

hdulist = fits.open('image0.fits')
data = hdulist[0].data

# Plot the 2D array
plt.imshow(data, cmap=plt.cm.viridis)
plt.xlabel('x-pixels (RA)')
plt.ylabel('y-pixels (Dec)')
plt.colorbar()
plt.show()
