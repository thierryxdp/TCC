def conta_frases (texto):
    """ conta o número de frases que aparece no dado de entrada, 'texto', 
    sendo que cada frase é terminada com um tipo de pontuação (ponto final,
    ponto de exclamação, ponto de interrogação ou reticências)
    str -> int """
    a = str.count (texto, '.')
    b = str.count (texto,'...')
    c = str.count (texto, '?')
    d = str.count (texto, '!')
    if b == 1:
        a = a-3
    if b == 2:
        a = a-6
    return a+b+c+d