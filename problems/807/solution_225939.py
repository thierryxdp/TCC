def conta_frases(texto):
    """função que dado um texto (str), retorna a quantidade de frases (int)"""
    return str.count(texto,".") + str.count(texto,"!")+str.count(texto,"?")+str.count(texto,"...")