def conta_frases(texto):
    fatiado = str.split(texto, '.' or '?' or '!' or '...')
    return len(fatiado)