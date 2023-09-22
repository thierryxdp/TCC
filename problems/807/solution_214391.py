def conta_frases(frase):
    """calcula o numero de frases que aparecem no texto"""
    return len(frase not in("!,...,?"))