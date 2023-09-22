def conta_frases(texto):
    '''Função que calcula e retorna o número de frases de 
    um texto dado na entrada
    str -> int'''
    return str.count(texto,'.',0)+str.count(texto,'!',0)+str.count(texto,'?',0)+1