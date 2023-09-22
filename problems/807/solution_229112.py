def conta_frases (texto):
    """função que conta o número de frases que aparecem no texto. sting--->int"""
    texto=len(str.split(texto,'.,!,...'))
    return texto