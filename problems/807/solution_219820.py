def conta_frases(texto):
    x=texto.split('.' and '...' and '?' or '!')
    return len(x) -1