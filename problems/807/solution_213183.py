def conta_frases (texto):
    """ conta o número de frases que aparece no dado de entrada, 'texto', 
    sendo que cada frase é terminada com um tipo de pontuação (ponto final,
    ponto de exclamação, ponto de interrogação ou reticências)
    str -> int """
    A = str.count (texto, '.')
    b = str.count (texto,'....')
    c = str.count (texto, '?')
    d = str.count (texto, '!')
    return a+b+c+d