def conta_frases(texto):
    """Retorna o numero de frases que aparecem num texto"""
    """str->int"""
    k = str.split(texto,'!')
    j = str.split(texto,'?')
    l = str.split(texto,'.')
    m = str.split(texto,'...')
    return len(k)+len(j)+ len(l)+len(m)