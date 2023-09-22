def lingua_p(palavra):
    '''Recebe uma palavra e retorna a tradução dela para
    língua do P
    str -> str'''
    nova_palavra = ''
    for i in range(0, len(palavra)):
        if palavra[i] in 'AaÁáEeÉéIiÍíOoÓóUuÚú':
            nova_palavra += palavra[i] + 'p' + palavra[i]
        else:
            nova_palavra += palavra[i]
    return nova_palavra