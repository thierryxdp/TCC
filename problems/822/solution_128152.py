def repetidos(numeros):
    ''' Função que recebe uma lista e retorna o número de vezes
    	que um elemento da lista é igual ao elemento anterior
    	list->int '''
    repetidos = 0
    prox = 0
    while prox <len(numeros):
        if numeros[prox] == numeros[prox +1]:
            repetidos = repetidos + 1
        prox= prox + 1
    return repetidos