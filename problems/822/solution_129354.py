def repetidos(lista):
    '''Recebe como entrada uma lista de números e 
    retorna a quantidade de vezes
	que um elemento da lista é igual ao elemento anterior.'''
    num_anterior == lista[0]
    n = 0
    proximo = 1
    while proximo < len(lista):
        if lista[proximo] == num_anterior:
            n = n + 1
        num_anterior = lista[proximo]
        proximo = proximo + 1 
    return n