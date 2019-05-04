import numpy
a = numpy.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
numpy.savetxt("guardar_01.csv", a, delimiter=",") 

a = numpy.arange(1,5,1,dtype=numpy.int8)
b = numpy.arange(1,5,1,dtype=numpy.int8) ** 2
c = numpy.arange(1,5,1,dtype=numpy.int8) ** 3
d = b + c


j = numpy.asarray([ a, b, c,d ])
print(type(j)) #numpy.ndarray
numpy.savetxt("guardar_03.csv", j, delimiter=",") 

z = j.transpose()


numpy.savetxt("guardar_04.csv", z, delimiter=",", fmt="%i") 


numpy.savetxt("guardar_05.csv", z, delimiter=",", fmt="%i", header='"n","n^2","n^3","(n^2)+(n^3)"') 
