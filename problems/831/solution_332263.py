def lingua_p(palavra):
    ''' Função que receba a mesma palavra traduzida para a língua P, str -> str'''
    for x in range(0, len(palavra)):
        if letra[x] in ['a', 'e', 'i', 'o', 'u']:
            letra.insert(x + 1, 'p')
            letra.insert(x + 2, letra[x])
            x = x + 2
    return letra