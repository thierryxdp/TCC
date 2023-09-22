def conta_frases(texto):
    '''função que retorna o número de frases contidas no texto
    str -> int'''
    return len(str.split(texto,'.', '...', '!', '?'))