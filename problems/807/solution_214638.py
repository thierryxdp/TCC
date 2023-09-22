def conta_frases(texto):
    '''função que dado um texto, retorna a quantidade de frases
       contidas neste texto. str -> int'''
    texto = str.replace(texto, '...', '@')
    return str.count(texto, '.') + str.count(texto, '@') + str.count(texto,'!') + str.count(texto,'?')