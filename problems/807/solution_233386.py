def conta_frases(texto):
    '''Conta o numero de frases que aparecem no texto.
    str-->int'''
    i = 0
    qnt = 0
    palavras = texto.split(' ')
    while i < len(palavras):
        if '?' or '!' or  '.'  in palavras[i]:
            qnt = qnt + 1
    	i = i + 1
        return qnt