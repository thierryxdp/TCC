# conta o número de frases de um texto
def conta_frases(texto):
    """str->str"""
    texto = texto.replace("!",".")
    texto = texto.replace("?", ".")
    texto = texto.replace("...",".")
    return texto.count(".")