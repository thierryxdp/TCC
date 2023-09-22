def conta_frases(texto):
    for k in ['.','...', '!', '?']:
        x=str.split(texto,k)
        return len(x)