def conta_frases(string):
    """
    Essa função ira retornar a quantidade de frases presente em um texto dado.
    str->int
    """
    numero_de_frases = str.count(string,'A','B','C','D')
    return numero_de_frases