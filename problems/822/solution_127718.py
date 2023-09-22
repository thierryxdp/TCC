def repetidos(lista):
    """
    funçao que recebe como entrada uma lista de numeros e retorna o numero de vezes
    que um elemento da lista é igual ao elementar anterior
    :param l(lista): list 
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