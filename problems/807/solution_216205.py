def conta_frases (texto):
    """função que dada um texto, retorne a quantidade de frases"""
    '''str -> int'''
    return len(str.partition(texto,'.','!','?')