def repetidos(numeros):
    i=0
    cont=0
    numeros.sort()
    while i<len(numeros):
        if numeros[i] == numeros[i]:
            cont=+1
        i=i+1
    return cont