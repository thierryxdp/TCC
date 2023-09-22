def conta_frases(texto):
    """função que recebe um texto(string) e retorna a quantidade de frases do mesmo"""
    textonovo = str.replace(texto,"...",".")
    return str.count(textonovo,".")+str.count(textonovo,"!")+str.count(textonovo,"?")