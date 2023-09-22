def conta_frases(texto):
    """Dado um texto armazenado em formato de string, essa função retorna
    a quantidade de frases que esse texto possui
    str-->int"""
    return str.count(texto,".")+str.count(texto,"?")+str.count(texto,"!")-2*str.count(texto,"...")