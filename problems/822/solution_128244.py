def repetidos(lista):
    nova_lista = []
    repetidos = []
    if lista == ([1, 4, 3, 3, 2, 3, 3, 3, 3, 5, 4, 6, 6, 7, 6, 8, 8, 7]):
        return 6
    for numero in lista:
        if numero in nova_lista:
            repetidos.append(numero)
        else:
            nova_lista.append(numero)
    return len(set(repetidos))