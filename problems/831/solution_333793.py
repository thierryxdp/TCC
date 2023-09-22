def lingua_p(palavra):
    '''A função recebe uma palavra em
    português e traduz para a língua do p
    str --> str'''

    traduz_p = []
    contagem = 0
    limit = len(palavra)

    while contagem < limit:
        if palavra[contagem] in 'aeiouáéíóú':
            traduz_p.append(palavra[contagem] + 'p' + palavra[contagem])
        else:
            traduz_p.append(palavra[contagem])

        contagem += 1

    return ''.join(traduz_p)