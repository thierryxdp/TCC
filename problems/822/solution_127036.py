def repetidos(lista):
    """A função retorna o número de vezes que um elemento da lista
    é igual ao anterior.
    list-->int."""
    i = 1
    ocorrencias = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            ocorrencias += 1
            i += 1
        else:
            i += 1
    return ocorrencias