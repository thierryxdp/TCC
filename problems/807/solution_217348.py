def conta_frases(texto):
    """Retorna o número de frases em um texto"""
    texto.replace("...",".")
    return texto.replace("...",".") str.count(texto,".")+str.count(texto,"!")+str.count(texto,"?")