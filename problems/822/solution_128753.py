def repetidos(lista):
    """
    """
    contador = 0
    for i in range(len(lista)):
        if lista[i] == lista[i+1]:
            contador += 1
        return contador