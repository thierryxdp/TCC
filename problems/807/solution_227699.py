def conta_frases(texto):
    '''
    Função conta quantas frases tem no texto inserido.
    str -> int
    '''
    pts = str.join('*', str.split(texto,'...'))
    a = str.count(pts,'.')
    b = str.count(pts,'!')
    c = str.count(pts,'?')
    d = str.count(pts,'*')
    total = a+b+c+d
    return total