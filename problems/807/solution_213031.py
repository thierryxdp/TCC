def conta_frases (texto):
    '''
    Retorna o valor de frases em
    um texto
    String -> int

    '''

    if texto.find("..."):
        return texto.count(".") + texto.count("!") + texto.count("?") - 3
    else:
        return texto.count(".") + texto.count("!") + texto.count("?")