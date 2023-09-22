def repetidos(numeros):
    i=0
    cont=0
    while i<len(numeros)-2:
        if numeros[i] == numeros[i+1]:
            cont=+1
        i=i+1
    return cont