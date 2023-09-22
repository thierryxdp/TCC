def conta_frases(frase):
    """volta o numero de frases representadas no texto str->int"""
    ponto = frase.split('.')
    excl = frase.split('!')
    inter = frase.split('?')
    retic = frase.split('...')
    return (len(ponto) - 2*retic) + len(excl) + len (inter)