def conta_frases(x):
    '''Retorna o número de frases do texto
    str -> int'''
    return  str.count(x,'!') + str.count(x,'?') + str.count (str.replace(x,'...', '.'),'.')