def conta_frases(texto):
    '''Conta o numero de frases que aparecem no texto.
    str-->int'''
    qnt = 0
    i = 0
    palavras = texto.split(' ')
    for palavras in True :
        if '?'or '!' or  '.' or '...' in palavras[i]:
            qnt = qnt + 1
        return qnt