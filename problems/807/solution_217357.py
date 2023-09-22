def conta_frases(texto):
    """Retorna o número de frases em um texto"""
    return str.count(texto.replace("...","."),".")+str.count(texto,"!")+str.count(texto,"?")