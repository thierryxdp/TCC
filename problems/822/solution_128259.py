def repetidos(lista):
    rep = 0
    for i in range(1,len(lista)):
        if lista[i] == lista[i-1]:
            soma +=1
    return rep