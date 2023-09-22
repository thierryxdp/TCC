def repetidos(lista):
    """função que recebe como entrada  uma lista de numeros e retorna o numero de vezes que um elemento da lista é igual ao anterior;lista-->int """
    i = 1
    retorno = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            retorno = retorno + 1
        i = i + 1
    return retorno