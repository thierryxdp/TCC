def conta_frases(texto):
    """função que conta o numero de frases que aparecem em um texto.
    str->int"""
   
    split = str.split(texto,('.','!','?'))
    frases = len(split)