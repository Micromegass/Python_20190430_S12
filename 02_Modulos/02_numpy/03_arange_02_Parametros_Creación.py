import numpy

desde = 10
hasta = 34

incrementos = 3

a = numpy.arange(desde,hasta,incrementos)
#a = numpy.arange(10,34,3)


print("a:",a)
print("len(a):",len(a))
print("type(a):",type(a))

print("-"*81)
for elemento in a:
    print(elemento)

print("-"*81)


for i in range(len(a)):
    t = "i:{0}, a[{0}] = {1}".format(i,a[i]) 
    print(t)


print("-"*81)
