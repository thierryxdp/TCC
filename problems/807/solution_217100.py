def conta_frases(texto):
    """A função recebe um texto e conta o numero de frases.
    str -> int"""
    return len(str.strip(texto,".!...?"))