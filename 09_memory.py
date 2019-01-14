import sys

a = 3
b = 3.123
c = [a, b]
d = []
for obj in [a, b, c, d]:
  print(obj, sys.getsizeof(obj))


'''When you run the code above, you will see that
 an integer uses 28 bytes, a float uses
 24 bytes, and a list of the two uses 80 bytes.'''

import numpy as np

a = np.zeros(5, dtype=np.int32)
b = np.zeros(5, dtype=np.float64)

for obj in [a, b]:
  print('nbytes         :', obj.nbytes)
  print('size x itemsize:', obj.size*obj.itemsize)
