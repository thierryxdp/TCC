def conta_frases(texo):
    """Função que conta o número de frases
    que aparecem no texto.
    str -> int"""
    frases = (str.count(texo,'!',0,-1))+(str.count(texo,'?',0,-1))+(str.count(texo,'.',0,-1))+(str.count(texo,'...',0,-1))
    return frases