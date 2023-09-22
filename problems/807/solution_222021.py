def conta_frases(texto):
    '''Retorna a quantidade de frases presente no texto inserido como parâmetro.
    str->int'''
    str.replace(texto,'...','.')
    str.replace(texto,'?','.')
    str.replace(texto,'!','.')
    return str.count(texto,'.')