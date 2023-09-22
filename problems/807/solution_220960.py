def conta_frases(frase):
    """Uma função que dado um texto, diz quantas frases tem"""
    """str -> int"""
    frase = frase.replace('...', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.split('  ')
    return frase