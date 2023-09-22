def repetidos(lista):
    i = 1
    repet = 0
    while i<len(lista):
        if lista[i-1] == lista[i]:
            repet +=1
        i+=1
    return repet