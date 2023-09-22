def conta_frases(texto):
    s=str.count(texto,'.')
    t=texto[len(texto)-1:].count('.')
    y=str.count(texto,'!')
    z=str.count(texto,'?')
    w=str.count(texto,'...')
    return x+y+z+w+t