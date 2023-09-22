def conta_frases(texto):
    """conta a quantidade de frases em um texto"""
    quant = texto.split(".","...","!","?")
    return len(quant)