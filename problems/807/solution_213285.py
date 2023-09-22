def conta_frases(texto):
    """Dado um texto, conta o número de frases que aparecem nesse texto. Cada frase no texto é terminada com um ponto, seja ele, final, de exclamação, interrogação ou reticencias
    entrada: str
    saida: str"""
    s=texto.split("!")
    x=texto.split("?")
    y=texto.split("!")
    return len(s), len(y), len(x)