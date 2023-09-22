def repetidos(lista):
    soma=1
    i=0
    while i<len(lista):
        soma+=soma
        if lista[i]==lista[i-1]:
            soma
        i=i+1
    return soma