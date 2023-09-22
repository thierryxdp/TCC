def conta_frases(texto):
    a=str.split(texto,'.')
    b=str.split(a,'!')
    c=str.split(b,'?')
    d=str.split(c,'...')
    return len(d)