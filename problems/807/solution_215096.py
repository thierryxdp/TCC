def conta_frases(texto):
    b = texto.slit("!",".","...","?")
    return len(b)