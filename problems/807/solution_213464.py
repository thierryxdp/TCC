def conta_frases(texto):
    """retorna o número de frases do texto. Cada frase é terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou reticências
    str->"""
    1=str.count(texto,.)
    2=str.count(texto,!)
    3=str.count(texto,?)
    4=str.count(texto,...)
    return (1+2+3+4)