def repetidos(lista_numeros):
    """ Dada a lista de entrada, retorne o número de vezes que um elemento da lista é igual ao elemento anterior"""
    n = 0
    qts_repetidos = ''
    while n <len(lista_numeros):
        if lista_numeros[n] == lista_numeros[n-1]:
            qts_repetidos = str.count(lista_numeros[n],)
        n = n + 1
    return qts_repetidos