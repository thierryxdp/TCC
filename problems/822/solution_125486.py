def repetidos(lista):
    i=1
    x=0
    while i<len(lista):
        if lista[i-1]==lista[i]:
            x=x+1
    return x