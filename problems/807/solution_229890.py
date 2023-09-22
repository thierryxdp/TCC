def conta_frases (texto):
    '''
    função que recebe um texto e retorna o numero de frases
    de acordo com a pontução presente no texto
    str-> int
    '''
    b = str.count(texto,'!')
    c = str.count(texto,'?')
    d = str.count(texto,'.')
    e = str.count(texto,'...')
    f = e - (3*e)
    return b + c+ d + f