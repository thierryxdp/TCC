def repetidos(lista):
    cont = 0
    for x in list(enumerate(lista)):
        for y in lista.index:
            if x[y] == x[y+1]
            cont += 1
    return cont