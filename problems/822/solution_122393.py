def repetidos(lista):
    i=0
    r=0
    while i<len(lista):
        if lista[i+1]==lista[i]:
            r=r+1
        i=i+1
        return r