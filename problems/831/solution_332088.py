def lingua_p(palavra):
    ''' Função que receba a mesma palavra traduzida para a língua P, str -> str'''
    vogais = ['a', 'e', 'i', 'o', 'u']
    for x in palavra:
        if x in vogais:
        list.insert(vogais, x + 1, 'p')
            x = x + 1
    return vogais