def conta_frases(texto):
    ''' '''
    a=str.count(texto,'.')
    b=str.count(texto,'...')
    c=str.count(texto,'.')+str.count(texto,'...')-2
    d=str.count(texto,'?')
    e=str.count(texto,'!')
    return a+b+c+d+e