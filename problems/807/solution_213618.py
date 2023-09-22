def conta_frases(texto):
    """Retorna o numero de frases presente no texto.
    str->int"""
    t=texto.replace('...','!')
    p=t.count('.')
    i=t.count('!')
    e=t.count('?')
    return p+i+e