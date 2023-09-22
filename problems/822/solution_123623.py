def repetidos(lista):
    cont = 0
    for x and y in list(enumerate(lista)):
        if x[y] == x[y+1]:
            cont += 1
    return cont