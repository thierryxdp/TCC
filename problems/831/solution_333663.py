def lingua_p(palavra):
    '''A função recebe uma palavra em
    português e traduz para a língua do p
    str --> str'''

    traduz_p = []
    counter = 0
    limit = len(palavra)

    while counter < limit:
        if palavra[counter] in 'aeiouáéíóú':
            traduz_p.append(palavra[counter] + 'p' + palavra[counter])
        else:
            traduz_p.append(palavra[counter])

        counter += 1

    return ''.join(traduz_p)