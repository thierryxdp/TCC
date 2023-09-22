def repetidos(lista):
    """ A funçao repetidos recebe como entrada uma lista de números, e retorna o número de vezes que um elemento da lista é igual ao elemento anterio.
    list --> int
    """
    i = 0
    resultado = 0
    while i<len(lista)-1:
        if lista[i] == lista[i+1]:
            resultado = resultado + 1
        i=i+1

    return resultado