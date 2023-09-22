def conta_frases(texto):
    """dado um texto retorna o número de frases que o compõe
    str-->int"""
    return str.count(texto,'?')+str.count(texto,'.')+str.count(texto,'...')+str.count(texto,'!')(-2*str.count(texto,'...'))