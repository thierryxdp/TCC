def repetidos(lista_numeros):
    """ Dada a lista de entrada, retorne o número de vezes que um elemento da lista é igual ao elemento anterior"""
    i = 0
    repeticao = 0
    while i < len(lista_numeros):
        if lista_numeros[i]==lista_numeros[i-1]:
            repeticao = repeticao + 1
    return repeticao