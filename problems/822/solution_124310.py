def repetidos(lista):
    a=len(lista)
    b=0
    lista=lista+["abc",]
    for i in range(a):
        if lista[i]==lista[i+1]:
            b=b+1
    return b