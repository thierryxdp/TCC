def conta_frases(texto):
    '''dado um texto, retorna a quantidade de frases;
    str -> int'''
 return str.count(texto, '.') + str.count(texto, '!') + str.count(texto, '?') + str.count(texto, '...') - 3* str.count(texto, '...')