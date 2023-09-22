def conta_frases(texto):
    '''Retorna o número de frases no texto dado;
    str -> int'''
    n1=str.count(texto[0],'.')
    n2=str.count(texto[0],'...')
    n3=str.count(texto[0],'?')
    n4=str.count(texto[0],'!')
    return n4+n3+n1-2*n2