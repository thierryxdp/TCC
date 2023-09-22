def repetidos(lista):
    i = 0
    s = 0
    while i<len(lista):
        if lista[i] == lista[(i+1)]:
            s = s + 1
        i = i +1
    return s