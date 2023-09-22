def repet(lista):
    i=0
    repet = []
    while i < len(lista):
        if lista[i] == lista[i-1]:
            repet.append(lista[i])
        i+=1
    return len(repet)