def conta_frases(texto):
    '''função que calcula e retorna quantas frases existem em um texto de entrada; str -> int'''
    
    str.replace(texto,'...','.')
    
    if '.' in texto:
        return str.count('.')