def repetidos(lista_num: list) -> int:
    """ Retorna quantas vezes um elemento da lista é igual o elemento anterior
    dada uma lista de números. """

    i = 1
    num_anterior = list()

    while ( i < len(lista_num)):
        if (lista_num[i] == lista_num[i - 1]):
            list.append(num_anterior,i)
        i += 1

    return len(num_anterior)