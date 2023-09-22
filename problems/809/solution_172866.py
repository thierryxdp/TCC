def intercala(lista1, lista2):
    """
    Gera uma lista, lista3, a partir da intercalação dos elementos de
    duas listas de tamanho 3, lista1 e lista2.
    list, list -> list.

    Parameters:
    lista1: Parâmetro do tipo lista (list);
    lista2: Parâmetro do tipo lista (list).

    Returns:
    Uma nova lista, lista3.
    """

    if (len(lista1) != 3) or (len(lista2) != 3):
        return ("Insira duas listas de tamanho 3. Tente novamente!")

    else:
        lista3 = (lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2])
        return lista3