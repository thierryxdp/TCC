def repetidos(lista):
    soma=1
    i=0
    while i<len(lista):
        if lista[i+1]==lista[i-1]:
            soma=1
        i=i+1
    return soma