def repetidos(lista: list)-> int:
    """Dada uma lista de números, a função retorna o número de vezes
    que um elemento da lista é igual ao elemento anterior"""
    i = 0
    numvezes = 0
    while (i < len(lista)):
        if (lista[i] == lista[i-1]):
            numvezes += 1
        i += 1
    return numvezes