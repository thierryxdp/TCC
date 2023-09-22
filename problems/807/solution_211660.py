def conta_frases (texto):
    ret = str.count(texto,'...')
    exc = str.count(texto,'!')
    inter = str.count(texto,'?')
    pf = str.count(texto, '.')-3*ret
    return ret+exc+pf+inter