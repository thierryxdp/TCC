def lingua_p(palavra):
    '''Retorna a palavra na lingua do p.
    str -> str'''
    cont = 0
    lis_palavra = list(palavra)
    while cont < len(lis_palavra):
        if str.lower(lis_palavra[cont]) not in 'bcdfghjklmnpqrstvwxyzç':
            list.insert(lis_palavra, cont, 'p' + lis_palavra[cont
        cont += 1
    return lis_palavra