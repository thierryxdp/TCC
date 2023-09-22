def repetidos (lista):
    repete=0
    p=1
    while p<len(lista):
        if lista[p-1] == lista[p]:
            repete=repete+1
        p=p+1
    return repete