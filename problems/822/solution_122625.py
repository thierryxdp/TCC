def repetidos(lista):
    '''descricao'''
    repeticoes = 0
    i = 0
    while i < len(lista):
        if lista[i] in '123456789':
            repeticoes = repeticoes + 1
        i = i + 1
    return repeticoes