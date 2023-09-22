def conta_frases(texto):
    for k in ['.','...', '!', '?']:
        x=str.strip(texto,k)
    return len(x)