def conta_frases(texto):
    if len(texto.split('.'))==1:
        return 1
    if len(texto.split('.'))>1:
        return len(texto.split('.'))