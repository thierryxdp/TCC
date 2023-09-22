def invert(frase):
    """ Função que dada uma frase, ela é retornada sem çetras maiusculas,
    e sem pontuação. str -> str"""
    import pontoExclamacao
    invertido = pontoExclamacao(frase) and frase.lower
    return invertido