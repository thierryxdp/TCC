def conta_frases(texto):
    """retorna o número de frases do texto. Cada frase é terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou reticências
    str->"""
    a=str.count(texto,.)
    b=str.count(texto,!)
    c=str.count(texto,?)
    d=str.count(texto,...)
    return (a+b+c+d)