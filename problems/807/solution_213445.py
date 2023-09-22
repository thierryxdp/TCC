def conta_frases(texto):
    s=("?","!",".","...")
    return str.count(texto,tuple(s))