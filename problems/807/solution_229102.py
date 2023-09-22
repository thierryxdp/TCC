def conta_frases (texto):
    """função que conta o número de frases que aparecem no texto. sting--->int"""
    texto=str.split(texto,'.','!','?','...')
    return len(texto)