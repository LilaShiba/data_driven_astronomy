https://www.coursera.org/learn/data-driven-astronomy/lecture/sWnWt/the-solution-improving-your-method

Another approach is to think more carefully about the problem we're trying to solve. Do we really need 200 by 200 pixels in an image? This is the kind of number that scientists often choose somewhat arbitrarily or they don't even think about at all, which is fine until we come up against a problem like this.

If, for example, we cut down our images to 50 x 50 pixels we'd reduce our data size by a factor of 16, which means we'd only need 12 GB of memory, rather than 192. This is a good solution if there are no important information in the outer parts of the images.

A third approach is to improve our algorithm. Currently the problem is that calculating the median requires us to store all the data in memory. Can we calculate a running median that doesn't need all of the data to be loaded in memory at the same time?

As each image comes in, take the value of each pixel in the image and bin it. Once all of the images have been processed, you end up with a histogram of counts for each pixel in the image.

Because the bins in the histogram are ordered, you can sum up the counts in the histogram starting from the smallest bin until you get to half the total number of numbers. You then use the value of the resulting bin as your median. We'll investigate this more in the lab.


[m31][https://www.spacetelescope.org/projects/fits_liberator/m31data/]
