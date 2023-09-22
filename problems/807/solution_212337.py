def conta_frases(texto):
    """ Faça uma função que dado um texto armazenado, retorne o numero de frases que aparecem nesse texto.
    """
    #texto armazenado = str.strip(texto)
    texto = str.split(texto)
    return len(texto)