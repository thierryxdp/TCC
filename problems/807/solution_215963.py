def conta_frases(texto):
    '''função que retorna o número de frases contidas no texto
    str -> int'''
    texto = str.replace(texto, '...', '#')
    texto = str.replace(texto, '.', '#')
    texto = str.replace(texto, '!', '#')
    texto = str.replace(texto, '?', '#')
    return texto.count('#')