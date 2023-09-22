def conta_frases(texto):
    """funcao que conta o numero de frases que vao aparecer no texto.
    str -> int"""
    texto = texto.replace("!", ".")
    texto = texto.replace("?", ".")
    texto = texto.replace("...", ".")
    return texto.count(".")