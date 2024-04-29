import sys
from LTP import calculate_ltp
import algoritmo
import alg

entrada=sys.argv[1]
salida=sys.argv[2]
cases=0
n,w1,w2=0,0,0
a=[]
def loadCases():
    fundamentals=None
    with open(entrada, 'r') as en:
        for linea in en:
            linea = tuple(map(int, linea.replace("\n",'').replace(' ',',').split(',')))
            if len(linea)==1:
                cases=int(linea[0])
            if len(linea)==3:
                #a.append(fundamentals)
                fundamentals=[]
                n,w1,w2=linea[0],linea[1],linea[2]
                a.append(fundamentals)
            if len(linea)==2:
                fundamentals.append(linea)
    return n,w1,w2,a
n,w1,w2,allCases=loadCases()

for i in allCases:
    print(alg.es_posible(i,w1,w2))
    
