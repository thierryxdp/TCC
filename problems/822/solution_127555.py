def repetidos(numeros):
    i=0
    while i<len(numeros):
        if numeros[i]==numeros[i+1]:
            numeros=1+numeros[i]
        i=i+1
    return numeros