def conta_frases (frases):
    '''recebe uma string, calcula e retorna o número de frases contidas nela'''
    '''string->int'''
    um = len(str.split(frases, '!'))
    dois = len(str.split(frases, '?'))
    tres = len(str.split(frases, '.'))
    return um + dois