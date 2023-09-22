def conta_frases(texto):
    '''Retorna o número de frases de um determinado texto;
    str -> int'''
    s=str.count
    textomod=str.replace(texto,'...','.')
    pfinal=s(textomod,'.')
    pinterrogacao=s(textomod,'?')
    pexclamacao=s(textomod,'!')
    return pfinal+pinterrogacao+pexclamacao