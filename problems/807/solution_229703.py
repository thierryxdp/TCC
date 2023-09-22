def conta_frases(string):
    """
    Essa função dado um texto ira retornar a quantidade
    de frases presentes no mesmo.
    str->int
    """
    numero_de_frases = str.count(string,'!') + str.count(string,'...') + str.count(string,'?') + str.count(string,'.')
    return numero_de_frases