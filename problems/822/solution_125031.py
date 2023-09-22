def repetidos(numeros):
    ''''''
    i=0
    vezes=0
    while i+1<len(numeros):
        if numeros[i] == numeros[i+1]:
            vezes+=1
        i+=1
    return vezes