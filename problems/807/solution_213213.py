def conta_frases (texto):
    '''Função que conta o numero de frases contida em um texto'''
    ''' str -> int '''

    texto = texto.replace("...", "!")
    return texto.count("!") + texto.count("?") + texto.count(".")