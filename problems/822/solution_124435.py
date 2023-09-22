def repetidos(lista):
    """ """
    i=0
    vezes=[]
    while i<len(lista):
        if lista[i]==lista[i-1]:
            vezes=vezes+[1]
        i=i+1
    return len(vezes)+1