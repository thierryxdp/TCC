def conta_frases(texto):
    if '...' in texto:
        texto.replace('...','.')
        return texto