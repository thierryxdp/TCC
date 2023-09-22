def conta_frases(texto):
    """função que conta o numero de frases que aparecem em um texto.
    str->int"""
    texto2=str(texto)
    split = str.split(texto2,('.','!','?'))
    frases = len(split)