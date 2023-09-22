def conta_frases(texto):
    '''Conta o numero de frases que aparecem no texto.
    str-->int'''
    frases = texto.split('!' or '.' or '?' or '...' )
    x = list.count(frases)