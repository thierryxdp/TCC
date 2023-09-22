def repetidos(lista):
    """
    """
    lista = lista.split()
    contador = 0
    for i in lista:
        if lista[i] == lista[i] + 1:
        contador += 1
    return contador