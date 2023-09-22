def conta_frases(texto):
    '''conta o numero de frases que aparecem no texto
    str -> int'''
    ponto = str.count(texto, '.')
    exclamacao = str.count(texto, '!')
    interrogacao = str.count(texto, '?')
    reticencias = str.count(texto, '...')
    
    return ponto -3*reticencias+reticencias+exclamacao+interrogacao