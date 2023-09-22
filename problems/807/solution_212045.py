def conta_frases(texto):
    '''função que calcula e retorna quantas frases existem em um texto de entrada; str -> int'''
    
    if '.' or '!' or '?' in texto:
        texto = str.replace(texto,'...','.')
        return str.count(texto, '.')+str.count(texto, '!')+str.count(texto, '?')