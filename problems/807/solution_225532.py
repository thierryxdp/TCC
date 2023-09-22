def conta_frases(texto):
    """Função que conta o número de frases que aparecem em um texto
    str -> int"""
    return texto.count("?") + texto.count("!") + texto.count(".") - (3*texto.count("...")) + texto.count(".")