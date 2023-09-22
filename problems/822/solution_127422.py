def repetidos(numeros):
    ''' Função que recebe uma lista e retorna o número de vezes
    	que um elemento da lista é igual ao elemento anterior
    	list->int '''
    iguais = 0
    seguinte = 0
    while seguinte <len(numeros):
        if numeros[seguinte] == numeros[seguinte +1]:
            iguais = iguais + 1
        seguinte= seguinte + 1
    return iguais