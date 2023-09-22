def conta_frases(texto):
    """calcula e retorna quantas frases há em um texto"""
    return str.count(texto,".")+str.count(texto,"!")+str.count(texto,"?")+str.count(texto,"...")