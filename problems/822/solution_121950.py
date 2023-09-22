def repetidos(numeros):
    resultados=1
    i=0
    while i<numeros:
        x=list.count(numeros,numeros[i])
        if x==1:
            return 0
        elif x>=2:
            return x/x
   	i+=1
    return numeros