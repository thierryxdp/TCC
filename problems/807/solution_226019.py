def conta_frases(texto):
    '''retorna o numero de frases dado um texto
    str --> int'''
    return str.count(texto,'. ')+str.count(texto,'...')+str.count(texto,'!')+str.count(texto,'?')+str.count(texto,'.',-1)