def conta_frases(texto):
    """conta o número de frases que aparece no texto"""
    texto = texto.replace("!", ".")
    texto = texto.replace("?", ".")
    texto = texto.replace("...", ".")
    return texto.count(".")