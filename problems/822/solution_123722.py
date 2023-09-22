def repetidos (lista):
    r=0
    i=0
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            r+=1
        i+=1
    return r