def conta_frases(texto):

    v = str.count(texto,'.')
    x = str.count(texto,'!')
    y = str.count(texto,'?')
    z = str.count(texto,'...') - 2
    return v+x+y+z