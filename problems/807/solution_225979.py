def conta_frases(texto):
    """função que recebe um texto(string) e retorna a quantidade de frases do mesmo"""
    str.replace(texto,"...",".")
    return str.count(texto,".")+str.count(texto,"!")+str.count(texto,"?")