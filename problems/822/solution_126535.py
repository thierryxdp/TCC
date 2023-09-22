def repetidos(lista_numeros):
    '''funçao que calcula e retorna o numero de vezes que um elemento da lista e igual ao elemento anterior.list->int'''
    proximo = 0
    numero = 0
    while proximo<len(lista_numeros):
        if lista_numeros[proximo - 1] == lista_numeros[proximo]:
            numero = numero + 1
        proximo = proximo + 1
    return numero