def repetidos(lista):
    i=0
    repet=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            repet=repet+1
        i=i+1
    return repet