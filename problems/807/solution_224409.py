def conta_frases(texto):
    """retorna a quantidade de frases presentes em um texto;
    str -> int"""
    return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')