def conta_frases(frase):
    """contabiliza o numero de frases de um texto"""
    frase = frase.replace('...','?')
    frase = frase.replace('!','?')
    frase = frase.replace('?','?')
    frase = frase.replace('.','?')
    return frase.count('?')