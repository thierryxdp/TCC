def conta_frases(texto):
    '''Conta o numero de frases que aparecem no texto.
    str-->int'''
    qnt = 0
    qnt = qnt + texto.count('.')
    qnt = qnt + texto.count('...')
    qnt = qnt + texto.count('?')
    qnt = qnt + texto.count('!')
    return qnt