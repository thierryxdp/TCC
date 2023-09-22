def conta_frases(frases):
    """funcao que conta o numero de frases de um determinado texto"""
    """ string->int"""
    frases= frases.replace("!",".")
    frases= frases.replace("...",".")
    frases= frases.replace("?",".")
    frases= frases.split(".")
    return len(frases)-1