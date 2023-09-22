def repetidos(lista):
    """
    """
    contador = 0
    for i in (lista):
        if i == lista[i + 1]:
            contador += 1
            return contador