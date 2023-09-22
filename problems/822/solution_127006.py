def repetidos(lista):
    i=0
    list.sort(lista)
    repete=0
    while i< len(lista):
        if lista[i] == lista[i+1]:
            repete+=1
        i+=1
    return repete