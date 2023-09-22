def conta_frases(texto):
    """Dado um texto, retorna o total de frases terminadas pelas pontuaçoes dadas
    str->int"""
    return str.count(texto,"?")+str.count(texto,"!")+str.count(texto,".")-2*str.count(texto,"...")