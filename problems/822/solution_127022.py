def repetidos(lista):
    i=0
    repete=0
    while i< len(lista):
        if lista[i] == lista[i-1] and i-1>=0:
                repete+=1
        i+=1
    return repete