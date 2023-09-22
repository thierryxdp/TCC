def repetidos(lista):
    '''Recebe como entrada uma lista de números, e retorna a quantidade de vezes
que um número é igual ao anterior.'''
    i = 0

    while i < len(lista):
        if lista[i] == lista[:-1]: