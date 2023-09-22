def repetidos(lista):
    i=0
    r=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            r=r+1
        i=i+1
        return r