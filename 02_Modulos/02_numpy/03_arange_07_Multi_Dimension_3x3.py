import numpy

def informar(el_vector):
    print("el_vector:",el_vector)
    print("len(el_vector):",len(el_vector))
    print("type(el_vector):",type(el_vector))
    print("el_vector.dtype:",el_vector.dtype)
    print("el_vector.size:",el_vector.size) #CUANTOS ELEMENTOS TIENE EL VECTOR
    print("el_vector.shape:",el_vector.shape) #Una Tupla con Dimensiones
    print("-"*81) 

a = numpy.arange(1,4,1,numpy.int8)
b = numpy.arange(2,7,2,numpy.int16)
c = numpy.arange(5,16,5,numpy.int16)

informar(a)
informar(b)
informar(c)

m_3_3 = numpy.asarray([a,b,c])
informar(m_3_3)
