def repetidos(lista):
    n=0
    soma=0
    while n<len(lista)-1:
        if lista[n+1]==lista[n]:
            soma+=1
        n+=1
    return soma