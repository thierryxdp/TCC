def conta_frases(texto):
    import string
    p = string.punctuation
    n=str.count(texto,p)
    return n + 1