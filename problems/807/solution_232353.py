def conta_frases (texto):
    '''função que recebe um texto e retorna o número
    de frases nesse texto. cada frase deve terminar com um
    ponto de interrogação, ponto final, reticências ou ponto de
    exclamação'''
    b = texto.replace('?','.')
    c = b.replace('...','.')
    d = c.replace('!','.')
    a = d.count('.')
    return a