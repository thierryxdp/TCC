def repetidos(lista):
    i=0
    r=0
    I=i-1
    while I<len(lista):
        if lista[i]=lista[i+1]:
            r=r+1
        i=i+1
        return r