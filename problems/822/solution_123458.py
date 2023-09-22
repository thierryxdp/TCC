def repetidos(lista):
    i = 1
    while lista > 0:
        i = i * lista
        lista = lista - 1
    return i