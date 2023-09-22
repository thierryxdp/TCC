def repetidos(lista):
    a=1
    b=0
    while a<len(lista):
        if lista[a]==lista[a-1]:
            b=b+1
        a=a+1
    return b