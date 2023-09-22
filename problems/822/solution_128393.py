def repetidos(lista):
    '''função que retorna o número de vezes em que um elemento da lista é igual ao anterior '''
    proximo = 1
    acumulador = 0
    while proximo < len(lista):
        if lista[proximo] == lista[proximo-1]:
            acumulador = acumulador + 1
            return acumulador
        if lista[proximo]!=lista[proximo-1]:
            acumulador = acumulador
    proximo = proximo +1
    return acumulador