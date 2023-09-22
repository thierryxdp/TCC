def repetidos(lista=[]):
    i=0
    for i in range(len(lista)):
        if i>0 and lista[i]==lista[i-1]:
            i=i+1
    return i