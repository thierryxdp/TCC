def conta_frases (f):
    '''....'''
    ponto = '.'
    exclamacao = !
    interrogacao = ?
    reticencias = '...'
    return f.count(ponto) + f.count(exclamacao) + f.count(interrogacao) + f.count(reticencias)