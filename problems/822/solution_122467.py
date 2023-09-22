def repetidos(lista):
    i = 0
    num = 0
    vezes= 0
    while i < len(lista):
        if lista[i] == num:
            vezes = vezes + 1
        num = lista[i]
        i = i + 1
    return vezes