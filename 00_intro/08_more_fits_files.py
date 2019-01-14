from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

def fits_view(arr):
    hdulist = fits.open(arr)
    print(hdulist.info())
    data = hdulist[0].data
    plot_fits(data)

    # Plot the 2D array
def plot_fits(data):
    plt.imshow(data, cmap=plt.cm.viridis)
    plt.xlabel('x-pixels (RA)')
    plt.ylabel('y-pixels (Dec)')
    plt.colorbar()
    plt.show()

count = 0
while count <= 11:
    fits_view('fits_00/image'+str(count)+'.fits')
    count += 1
