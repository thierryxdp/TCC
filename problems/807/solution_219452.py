def conta_frases(texto):
    '''Retorna o número de frases no texto inserido
str -> int'''
    return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')+str.count(texto,'...')-(str.count(texto,'...')*3)