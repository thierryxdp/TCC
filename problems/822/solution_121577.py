def repetidos(lista):
    i=1
    n=0
    a=0
    while i<len(lista):
        if lista[i]==lista[n]:
            a+=1
            i+=1
            n+=1
        else:
            i+=1
            n+=1
    return a