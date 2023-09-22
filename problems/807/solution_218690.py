def conta_frases(texto):
    """inserindo um texto mostra o numero de frases que ele tem"""
    for pontuacao in ("...","!","?","."):
        texto = texto.replace(pontuacao,"!  ")
    return len(texto.split("!  "))-1