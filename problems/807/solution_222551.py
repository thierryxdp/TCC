def conta_frases(texto):
    '''Esta função conta o número de frases que compõem um texto.
    Instruções: Digite todo o texto entre aspas.
    str -> int'''
    conjunto_1 = str.count(texto, '.')
    conjunto_2 = str.count(texto, '!')
    conjunto_3 = str.count(texto, '?')
    conjunto_4 = str.count(texto, '...')
    if conjunto_4 >= 1:
        conjunto_1 = conjunto_1 - (conjunto_4*3)
    else:
        conjunto_1 = str.count(texto, '.')
    frases = conjunto_1 + conjunto_2 + conjunto_3 + conjunto_4
    return frases