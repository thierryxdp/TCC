def conta_frases(texto):
    import string
    p = string.punctuation
    return str.count(texto,p)