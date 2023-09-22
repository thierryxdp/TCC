def conta_frase(texto):
    """Retorna o numero de frases que aparecem num texto"""
    """str->int"""
    k = str.split(texto,'!')
    return len(k)