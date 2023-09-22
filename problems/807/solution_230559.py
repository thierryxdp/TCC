def conta_frases(texto):
    fatiado = str.split(texto, '.' and '?' and '!' and '...')
    return len(fatiado)