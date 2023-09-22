def repetidos(lista):
    c=0
    f=0
    while c<len(lista):
        if lista[c-1]==lista[c]:
            f+=1
        c=c+1
    return f