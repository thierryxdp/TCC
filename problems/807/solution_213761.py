def conta_frases(texto):
    """Calcula e retorna a quantidade de frases de um texto. str->float"""
    return str.count(texto,".")+str.count(texto,"?")+str.count(texto,"!")-2*str.count(texto,"...")