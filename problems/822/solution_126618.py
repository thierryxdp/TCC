def repetidos(lista):
    n = 0
    cont = 0
    while n < len(lista):
        if lista[n] == lista[n-1]:
            cont = cont + 1
        n = n + 1
    return cont