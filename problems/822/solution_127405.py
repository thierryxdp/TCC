def repetidos(numeros):
    ''' Função que recebe uma lista e retorna o número de vezes
    	que um elemento da lista é igual ao elemento anterior
    	list->int '''
    iguais = 0
    seguinte = 0
    while seguinte <len(numeros):
        if numeros[seguinte +1] == numeros[seguinte]:
            iguais = iguais + 1
    return iguais