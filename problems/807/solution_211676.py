def conta_frases(texto):
    '''Retorna o número de frases no texto dado;
    str -> int'''
    n1=str.count(texto,'.')
    n2=str.count(texto,'...')
    n3=str.count(texto,'?')
    n4=str.count(texto,'!')
    return n4+n3+n1-2*n2