def conta_frases (texto):
    """Dado um texto, conta o numero de frase que aparecem no mesmo, cada frase no texto é temrinada com um ponto, seja ele final, de exclamação, de interrogação ou reticencias
    entrada: str
    saida: str"""
    x=len(texto.split("?"))
    y=len(texto.split("!"))
    z=len(texto.split("."))
    return x+y+z