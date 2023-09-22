def conta_frases(texto):
    x=str.count(texto,'. ')
    t=texto[len(texto)-1:].count('.')
    y=str.count(texto,'!')
    z=str.count(texto,'?')
    w=str.count(texto,'... ')
    return x+y+z+t