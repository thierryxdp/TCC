def conta_frases(texto):
    '''Define o número total de frases no texto
    str -> int'''
    texto = texto 
    return str.count(texto, '.') + str.count(texto, '!') + str.count(texto, '?') - 2*str.count(texto, '...')