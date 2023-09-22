def conta_frases(texto):
    '''Conta o numero de frases que aparecem no texto.
    str-->int'''
    frases = texto.split()
    x = list.count(frases, '!' or '.' or '...' or '!' or ?')
    return x