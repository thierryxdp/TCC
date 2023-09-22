def repetidos(lista):
    i = 0
    cont = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            cont = cont + 1
        i = i + 1
    return cont