def repetidos(lista):
    """
    """
    lista = lista.split()
    contador = 0
    for i in range(lista):
        if lista[i] == lista[i] + 1:
        contador = contador + 1
    return contador