def conta_frases(x):
    """Função que conta o número de frases que aparecem neste texto.
    Cada frase no texto é terminada com um ponto final, um ponto de exclamação,
    um ponto de interrogação ou três pontos em sequência (reticências).
    str -> int """
    x = str.replace(x,'...','.')
    return str.count(x,'!') + str.count(x,'?') + str.count(x,'.')