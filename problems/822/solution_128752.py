def repetidos(lista):
    """
    """
    contador = 0
    for i in range(len(lista)):
        if i == i+1:
            contador += 1
        return contador