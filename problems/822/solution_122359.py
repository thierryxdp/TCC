def repetidos(lista):
    ''' Retorna o numero de vezes que um elemento da lista é igual ao seu anterior'''
    i = 1
    soma = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
        	soma = soma + 1
        i = i + 1
    return soma