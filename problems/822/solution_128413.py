def repetidos(lista):
    i = 0
    s = 0
    while (i)<len(lista):
        if lista[i] == lista[i]:
            s += 1
        i = i +1
    return s