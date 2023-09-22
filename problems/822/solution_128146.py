def repetidos(lista):
    """
    Essa função recebe uma lista de números, e retorna o 
    número de vezes que um elemento da lista é igual ao 
    elemento anterior.
    Parametros de entrada: list
    Valor de retorno; int
    """

    i = 0
    rep = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            rep = rep + 1
        i = i + 1
    return rep