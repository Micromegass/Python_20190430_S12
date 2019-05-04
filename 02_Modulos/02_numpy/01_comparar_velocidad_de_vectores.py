import sys
from datetime import datetime
import numpy

def numpysum(n):
    a = numpy.arange(n) ** 2
    b = numpy.arange(n) ** 3
    c = a + b
    return a,b,c

def pythonsum(n):
    a = []
    b = []
    c = []
    for i in range(n):
        a.append(i ** 2)
        b.append(i ** 3)        
        c.append(a[i] + b[i])
    return a,b,c


#size = int(sys.argv[1])

size = 1290 #En Windows 32 Virtual ya no funcionan desde 1291

start = datetime.now()
a,b,c = pythonsum(size)
delta = datetime.now() - start
print( "The last 2 elements of the sum", c[-2:])
print( "PythonSum elapsed time in microseconds", delta.microseconds)
print()


start = datetime.now()
a,b,c = numpysum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("NumPySum elapsed time in microseconds", delta.microseconds)


