def conta_frases(texto):
    """Função que retorna a quantidade de frases que há em um tesxto. str -> int + str"""
    t = texto + " "
    return str.count(t,'. ') + str.count(t,'!') + str.count(t, '?')