def repetidos(lista):
    i=1
    z=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            z+=1
        i=i+1
    return z