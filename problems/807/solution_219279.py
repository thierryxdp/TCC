def conta_frases(texto):
    """conta o número de frases em um texto
    str->int"""
    return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')+str.count(texto,'...')