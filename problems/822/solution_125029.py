def repetidos(numeros):
    ''''''
    i=0
    prox=i+1
    vezes=0
    while i<len(numeros):
        if numeros[i] == numeros[prox]:
            vezes+=1
        i+=1
    return vezes