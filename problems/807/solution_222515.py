def conta_frases(texto):
    """funcao que dado um texto de entrada, retorna o seu
    numero de frases;
    str -> int"""
    
    return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'...')