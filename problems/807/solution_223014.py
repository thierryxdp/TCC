def conta_frases(t):
    """Dado um texto "t", retorna o número de frases contidas nele
    sabendo que cada frase pode terminar com ".","?","..." ou"!"
    str -> int"""
    f = str.count(t,".")+str.count(t,"...")+str.count(t,"?")+str.count(t,"!")
    return f