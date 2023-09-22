def repetidos(lista):
    soma=1
    i=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            soma=1
        i=i+1
        if lista[i]!=lista[i-1]:
            soma=0
    return soma