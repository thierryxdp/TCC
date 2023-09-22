def conta_frases(texto):
    '''função que, dado um texto, conta o 
    número de frases contidas nele
    str -> int'''
    texto = str.replace(texto,'!','.')
    texto = str.replace(texto,'?','.')
    texto = str.replace(texto,'...','.')
    x = str.split(texto,'. ')
    return len(x)