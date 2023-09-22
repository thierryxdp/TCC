def conta_frases(texto):

    v = str.count(texto,'.')
    x = str.count(texto,'!')
    y = str.count(texto,'?')
    z = str.count(texto,'... ') 
    return v+x+y+z