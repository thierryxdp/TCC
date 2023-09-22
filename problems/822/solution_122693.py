def repetidos(lista):
    c=1
    a=0
    while c<len(lista):
        if lista[c]==lista[c-1]:
            a= a+1
        c=c+1
    return a