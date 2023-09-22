def repetidos(lista):
    '''Recebe uma lista com números e retorna o número de vezes que um
    elemento da lista é igual ao elemento anterior'''
    contador = 0
    proximo = 0
    while proximo < len(lista):
        if lista[proximo - 1] == lista[proximo]:
            contador = contador + 1
            proximo = proximo + 1
        return contador