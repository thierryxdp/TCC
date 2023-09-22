def repetidos(lista):
    '''Retorna a quantidade de vezes que um elemento da lista é igual ao seu anterior
    	list -> int'''
    i = 0
    iguais = 0
    while i < len(lista):
        if lista[i] == lista[i+1]:
            iguais = iguais + 1
        i = i+1
    return iguais