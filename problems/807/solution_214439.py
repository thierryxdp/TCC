def conta_frases(texto):
    """função que dado um texto retorna a quantidade de frases que ele contém; str-> int"""
    x = texto.count(".") + txt.count("!") +  txt.count("?")
    return x