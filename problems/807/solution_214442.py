def conta_frases(texto):
    """função que dado um texto retorna a quantidade de frases que ele contém; str-> int"""
    conta_texto = texto.count(". ") + texto.count("! ") +  texto.count("? ")
    return conta_texto