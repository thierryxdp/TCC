def conta_frases(texto):
    a=str.count(texto,'...')
    b=str.count(texto,'?')
    c=str.count(texto,'!')
    d=str.count(texto,'.')
    return -3*a+a+b+c+d