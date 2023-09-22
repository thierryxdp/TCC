def conta_frases(texto):
    
    for pontuacao in ("...","!","?","."):
        texto = texto.replace(pontuacao,"!  ")
    return len(texto.split("!  "))-1