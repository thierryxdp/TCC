def conta_frases(texto):
    b = texto.split("!",".","...","?")
    return len(b)