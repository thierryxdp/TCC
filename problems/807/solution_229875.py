def conta_frases (texto):
    b= str.count(texto,'.')
    c = str.count(texto,'!')
    d = str.count(texto,'...')
    e = str.count(texto,'?')
    f = (3*e)
    return  b + c+ d + f