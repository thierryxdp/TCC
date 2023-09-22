def conta_frases (texto):
    a = str.split(texto,',')
    b = str.split(texto,'.')
    c = str.split(texto,'!')
    d = str.split(texto,'...')
    e = str.split(texto,'?')
    f = str.split(texto,';')
    return  a + b + c+ d + e + f