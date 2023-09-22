def conta_frases(string):
    """Função que retorna a quantidade de frases de uma string"""
    s = string + " "
    return str.count(s,'. ') + str.count(s,'!') + str.count(s, '?')