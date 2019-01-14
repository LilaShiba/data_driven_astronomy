from statistics import mean
fluxes = [17.3, 70.1, 22.3, 16.2, 20.7]
m = mean(fluxes)
print(m)

# To calculate the median of a list without using the
# statistics module, you need to sort the data and take
# the central value:

fluxes = [17.3, 70.1, 22.3, 16.2, 20.7]
fluxes.sort()
mid = len(fluxes)//2
median = fluxes[mid]
print(median)

# This only works if you have an odd number of elements.
# If there are an even number of elements there are two
# middle ones, so you have to find both and take their
# average:

fluxes = [17.3, 70.1, 22.3, 16.2, 20.7, 19.3]
fluxes.sort()
mid = len(fluxes)//2
median = (fluxes[mid - 1] + fluxes[mid])/2
print(median)


fluxes = [17.3, 70.1, 22.3, 16.2, 20.7, 19.3]

def list_stats(a):
    a.sort()
    length = len(a)
    mid = int(length/2)
    mean = sum(a)/length
    
    if length == 1:
      return (a[0],a[0])

    if length % 2 == 0:
        median = (a[mid] + a[mid -1])/2
    else:
        median = a[mid]

    return median, mean




print(list_stats(fluxes))
