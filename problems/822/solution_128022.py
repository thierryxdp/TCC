def repetidos(numeros):
    '''Função que recebe uma lista de números e retorna o número
    de vezes que um elemento da lista é igual ao elemento anterior.
    list -> int'''
    cont = 0
    a = 1
    while a < len(numeros):
        if numeros[a] == (numeros[a-1]):
            numeros.count(numeros[a])
            cont += 1
        a += 1
    return cont