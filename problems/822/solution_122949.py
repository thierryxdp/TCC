def repetidos(lista):

    """ Queremos uma função que nos retorne a quantidade de vezes que, em uma lista, temos
        números repetidos. O índice começa em 1 e temos um acumulador que contabiliza a quantidade
        de vezes que temos números repetidos.

        list -> int
    """

    i=1
    vezes_repetidas = 0
    
    while i<len(lista):
        if (lista[i] == lista[i-1]):
            vezes_repetidas = vezes_repetidas + 1
        i=i+1
    return vezes_repetidas