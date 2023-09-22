def conta_frases(texto):
    '''Função que calcula e retorna o número de frases de 
    um texto dado na entrada
    str -> int'''
    return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')+1