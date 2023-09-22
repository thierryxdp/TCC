def lingua_p(palavra):
    ''' Função que receba a mesma palavra traduzida para a língua P, str -> str'''
    vogais = ['a', 'e', 'i', 'o', 'u']
    lista = []
    for x in palavra:
        if palavra in vogais:
            list.insert(vogais, x + 1, 'p')
            x = x + 1
        if palavra in vogais:
            list.insert(vogais, x + 2, lista[x])
            x = x + 2
    return lista