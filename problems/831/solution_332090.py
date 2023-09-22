def lingua_p(palavra):
    ''' Função que receba a mesma palavra traduzida para a língua P, str -> str'''
    vogais = ['a', 'e', 'i', 'o', 'u']
    lista = []
    for x in palavra:
        if lista in vogais:
            list.insert(vogais, x + 1, 'p')
            x = x + 1
    return vogais