def repetidos(lista):
    i = 0
    s = 0
    while (i-1)<len(lista):
        if lista[i] == lista[i+1]:
            s += 1
        i = i +1
    return s