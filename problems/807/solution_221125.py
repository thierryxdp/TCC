def conta_frases(texto):
    a=str.count(texto,'.')
    b=str.count(texto,'!')
    c=str.count(texto,'?')
    d=str.count(texto,'...')
    return a+b+c-2*d