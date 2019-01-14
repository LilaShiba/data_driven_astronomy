import numpy as np
# input is an array of csv files
def mean_datasets(filenames):
  n = len(filenames)
  data = np.loadtxt(filenames[0], delimiter=',')
  # create one large array
  for i in range(1,n):
    data += np.loadtxt(filenames[i], delimiter=',')
  # return the mean of the set of data
  return np.round(data/n, 1)
