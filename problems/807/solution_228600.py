def conta_frases(texto):
    for k in ['.','...', '!', '?']:
        z=texto[:]
        x=str.split(z,k)
    return len(x)