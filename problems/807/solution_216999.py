def conta_frases(frases):
    """funcao que conta o numero de frases dado determinado texto qualquer que sao identificadas por . ! ? e ..."""
    """ string->innt"""
    frases= frases.replace("!",".")
    frases= frases.replace("...",".")
    frases= frases.replace("?",".")
    frases= frases.split(".")
    return len(frases)-1