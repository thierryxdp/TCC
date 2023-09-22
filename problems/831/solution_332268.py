def lingua_p(palavra):
    ''' Função que receba a mesma palavra traduzida para a língua P, str -> str'''
    letra = 0
    vogais = list(['a', 'e', 'i', 'o', 'u'])
    for x in range(len(palavra)):
        if letra[x] in vogais:
            letra.insert(x + 1, 'p')
            letra.insert(x + 2, letra[x])
            x = x + 2
    oracao = ''.join(letra)
    return letra