def repetidos(lista):
    """
    funçao que dada uma lista numerica verifica a posiçao de um
    numero e retorna a quantidade de vezes que um elemento da
    lista e igual ao elemento anterior.
    :param lista: list 
    :return: int 
    """
    indice = 0
    contando = 0
    repetindo = 0
    while contando < len(lista):
        if lista[indice] == lista[indice - 1]:
            repetindo += 1

        indice += 1
        contando += 1

    return repetindo