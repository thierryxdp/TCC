def conta_frases (texto):
    a = str.count (texto,',')
    b = str.count(texto,'.')
    c = str.count(texto,'!')
    d = str.count(texto,'...')
    e = str.count(texto,'?')
    f = (3*e)
    return  a + b + c+ d + f