def repetidos(num):
    '''recebe uma lista de numeros e retorna o numero de vezes que um elemento da lista
    é igual a um anterior
    list --> int'''
    i = 1
    repeticoes = 0
    while i < len(num):
        if lista[i - 1] == lista[i]:
            repeticoes = repeticoes + 1
    return repeticoes