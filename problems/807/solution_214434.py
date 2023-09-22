def conta_frases(texto):
    """função que dado um texto retorna a quantidade de frases que ele contém; str-> int"""
    frases_separadaspto=texto.split('. ')+texto.split('! ')+texto.split('? ')
    return len(frases_separadaspto)