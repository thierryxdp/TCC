def par(numero):
    'retorne o numero dado é par. int'
    return numero%2==0

def filtra_pares(tup):
    'dados uma tupla com 4 elementos retorne apenas os numeros pares.tupla-->tupla'
    
    
    if par(tup[0]):
        resultado0= tup
    else:
        resultado0 =tup[1:3]
    if par(tup[1]):
        resultado1= tup[1]
    else:
        resultado1= tup[0:1] + tup[2:]
        
    if par(tup[2]):
        resultado2= tup[2]
    else:
        resultado2= tup[0:2] + tup[3:]
    if par(tup[3]):
        resultado3= tup[3]
    else:
        resultado3 =tup[0:3]  
    return (resultado0,resultado1,resultado2,resultado3)