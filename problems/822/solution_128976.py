def repetidos(lista):
    listaf=[ ]
    i=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            lista[i]==listaf
        i=i+1
    return len(listaf)