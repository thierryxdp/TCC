def conta_frases(x):
    """Dado um texto, retorna quantas frases contém, porém cada frase é terminanda com ponto final, ponto de exclamação, ponto de interrogação ou três pontos; str -> str"""
    x= str.replace(x,"...","!")
    return str.count(x,".")+str.count(x,"!")+str.count(x,"?")