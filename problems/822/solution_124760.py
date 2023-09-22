def repetidos(lista:list)->int:
    rep = 0
    for c in range(1,len(lista)):
        if lista[c] == lista[c-1]:
            rep+=1
    return rep