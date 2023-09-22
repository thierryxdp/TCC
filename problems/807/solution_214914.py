def conta_frases(frase):
    """Retorna a quantidade de frases que tem no período.str->int"""
    return str.count(frase,".","...","!","?")