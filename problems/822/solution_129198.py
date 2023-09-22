def repetidos(lista=[]):
    i=0
    for x in range(len(lista)):
        if x>0 and lista[x]==lista[x-1]:
            i=i+1
    return i