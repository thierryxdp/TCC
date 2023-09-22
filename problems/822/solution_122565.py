def repetidos(lista):
    c=0
    d=0
    while c<len(lista):
        if lista[c]==lista[c+1]:
            d=d+1
        c=c+1
    return