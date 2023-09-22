def repetidos(lista):
    i = 0
    s = 0
    while (i-1)<len(lista):
        if lista[i-1] == lista[i]:
            s += 1
        i = i +1
    return s