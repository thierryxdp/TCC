def conta_frases(frases):
    """função que dado um texto, retorne o número de frases que o texto possui; string -->int"""
    frase= frase.slipt(".","!","?","...")
    return len(frase)