def repetidos(numeros):
    repetido = 0
    for i in range(len(numeros)):
        if numeros[i-1]==numeros[i]:
            repetido+=1
    return repetido