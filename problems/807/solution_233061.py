def conta_frases(frase):
    """volta o numero de frases representadas no texto str->int"""
    ponto = frase.split('.')
    exclama = frase.split('!')
    interro = frase.split('?')
    reticen = frase.split('...')
    return (len(ponto) - 2*reticen) + len(exclama) + len (interro)