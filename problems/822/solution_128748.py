def repetidos(lista):
    """
    """
    contador = 0
    for i in (lista):
        if i == lista[i+1]:
            contador = contador + 1 
        return contador