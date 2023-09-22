def conta_frases(texto):
    import string
    p = string.punctuation
    n = texto.split(p)
    return p