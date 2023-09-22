def conta_frases(texto):
    '''Esta função conta o número de frases que compõem um texto.
    Instruções: Digite todo o texto entre aspas.
    str -> int'''
    frases = str.count(texto, '.')
    return frases