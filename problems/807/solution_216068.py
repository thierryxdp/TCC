def conta_frases(texto):
    '''função que conta o número de frases que aparecem no texto
    str->int'''
    P=str.count(texto,'.')
    E=str.count(texto,'!')
    I=str.count(texto,'?')
    R=str.count(texto,'...')
    return P+E+I+R