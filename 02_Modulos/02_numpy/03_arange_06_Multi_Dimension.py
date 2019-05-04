import numpy

def informar(el_vector):
    print("el_vector:",el_vector)
    print("len(el_vector):",len(el_vector))
    print("type(el_vector):",type(el_vector))
    print("el_vector.dtype:",el_vector.dtype)
    print("el_vector.size:",el_vector.size) #CUANTOS ELEMENTOS TIENE EL VECTOR
    print("el_vector.shape:",el_vector.shape) #Una Tupla con Dimensiones
    print("-"*81) 

a = numpy.arange(10,-10,-2,numpy.int8)
b = numpy.arange(10,101,10,numpy.int16)

informar(a)
informar(b)

m = numpy.asarray([a,b])
informar(m)


for vector in m:
    print(vector)
    for elemento in vector:
        print(elemento)

print("*"*81)

dimension = m.shape

print("dimension:",dimension)

filas,columnas = dimension
total_de_elementos = filas*columnas

print("filas:",filas,"columnas:",columnas,"total_de_elementos:",total_de_elementos)


print("*"*81)


for i in range(filas):
    for k in range(columnas):
        t = "m[{0},{1}] = {2}".format(i,k,m[i,k])
        print(t)
  
print("*"*81)
print(m)


