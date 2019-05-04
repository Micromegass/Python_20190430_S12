LA = [5, 10, 15, 20]
LB = [30, 35, 40, 45]
 
LC = list(map(lambda num1,num2: num1+num2, LA,LB)) #map applies this function to the two lists
 
print(LA,LB,LC)

def Sume_Listas(L1,L2):
    nueva = list()
    for pos in range(len(L1)):
        nueva.append(L1[pos]+L2[pos])
    return  nueva

LC = Sume_Listas(LA,LB)
print(LA,LB,LC)





##reuse lambda
La_lam = lambda n1, n2: n1+n2
print(La_lam(5,3))

LC = list(map(La_lam, LA,LB)) #map applies this function to the two lists
print
