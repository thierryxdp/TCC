def repetidos(numeros):
    ''''''
    i=0
    cont=0
    while i<len(numeros):
        if numeros[i-1] == numeros[i] :
            cont=cont+1
        i=i+1
    return cont