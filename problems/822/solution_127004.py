def repetidos(lista):
    i=0
    repete=[list.count(lista,lista[1])]
    while i< len(lista):
        if list.count(lista,lista[i]) > repete:
            repete=list.count(lista,lista[i])
        i+=1
    return repete