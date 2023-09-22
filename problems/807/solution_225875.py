def conta_frases(texto):
    """Retorna o numero de frases que aparecem no texto. Entrada:string"""
    texto = texto.replace("!", ".")
    texto = texto.replace("?", ".")
    texto = texto.replace("...", ".")
    return texto.count(".")