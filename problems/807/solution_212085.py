def conta_frases(texto):
    """Função que dado um texto, retorna a quantidade de frases (terminadas
com ponto final, ponto de exclamação, ponto de interrogação ou reticências.
    str -> int"""
    return str.count(texto, '. ') + str.count(texto, '! ') + str.count(texto, '? ') + 1