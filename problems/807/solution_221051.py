def conta_frases (frases):
    '''recebe uma string, calcula e retorna o número de frases contidas nela'''
    '''string->int'''
    return len(str.split(frases, '!')) and len(str.split(frases, '?'))