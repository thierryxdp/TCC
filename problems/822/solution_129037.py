def repetidos(lista):
    '''Recebe uma lista com números e retorna o número de vezes que um
    elemento da lista é igual ao elemento anterior'''
    contador = 0
    proximo = 0
    numeros = lista.split()
    while proximo < len(numeros):
        if numeros[proximo - 1] == numeros[proximo]:
            contador = contador + 1
        proximo = proximo + 1
        return contador