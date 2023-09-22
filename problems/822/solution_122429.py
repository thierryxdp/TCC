def repetidos (lista):
    a = 0
    b = 1
    cont = 2
    while b < len(lista):
        if lista[a] == lista[b]:
            cont += 1
        a += 1
        b += 1
    return cont