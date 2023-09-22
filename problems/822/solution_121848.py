def repetidos(lista):
    i=1
    r=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            r+=1
        i+=1
    return r