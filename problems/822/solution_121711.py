def repetidos(lista):
    '''Dado uma lista de números, retorna o número de vezes que um elemento da lista é igual ao elemento anterior'''
    y = 1
    repeticao = 0
    while y < len(lista):
        if lista[y] == lista[y-1]:
            repeticao = repeticao + 1
        y = y + 1
    return repeticao