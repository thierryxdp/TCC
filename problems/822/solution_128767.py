def repetidos(lista):
    """
    	Recebe uma lista e retorna a quantidade vezes em que
        o elemento atual é igual ao elemento anterior.
        list --> int
    """
    elementoAnterior = ''
    cont = 0
    for elemento in lista:
        if elemento == elementoAnterior:
            cont += 1
        elementoAnterior = elemento
    return cont