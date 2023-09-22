def conta_frases(texto):
    """dado um texto, a função conta o número de frases que aparecem neste texto. Frases podem ser terminadas por ponto
    final, exclamação, interrogação ou reticências. OBS.: não se pode terminar uma frase com interrogação ou exclamação
    repetidos em sequência; string -> int"""
    return str.count(str.replace(texto,"...","."),".") + str.count(texto,"?") + str.count(texto,"!")