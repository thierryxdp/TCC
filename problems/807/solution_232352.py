def conta_frases (texto):
    '''função que recebe um texto e retorna o número
    de frases nesse texto. cada frase deve terminar com um
    ponto de interrogação, ponto final, reticências ou ponto de
    exclamação'''
    texto.replace('?','.')
    texto.replace('...','.')
    texto.replace('!','.')
    a = texto.count('.')
    return a