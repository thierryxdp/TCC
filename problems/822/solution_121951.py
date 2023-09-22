def repetidos(numeros):
    resultados=1
    i=0
    while i<numeros:
        x=list.count(numeros,numeros[i])
        if x==1:
            resultados-=resultados
        elif x>=2:
            resultados/=resultados
   	i+=1
    return numeros