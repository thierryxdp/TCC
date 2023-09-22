def conta_frases(texto):
    """Conta o número de frases que aparecem no texto. string -> int"""
    return str.count(texto,".")+str.count(texto,"...")+str.count(texto,"!")+str.count(texto,"?")