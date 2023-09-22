def conta_frases (texto):
    '''Função que conta o numero de frases contida em um texto'''
    ''' str -> int '''

    return texto.count(texto.replace ('...', '!')) + texto.count (".") + texto.count ("!") + texto.count ("?")