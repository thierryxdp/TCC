def repetidos(lista):
    """
    """
    contador = 0
    for i in range(0,len(lista)):
        if lista[i] == lista[i + 1]:
            contador += 1
    return contador