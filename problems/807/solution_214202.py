def conta_frases(texto):
    """função que dado um texto retorna a quantidade de frases que ele contém; str-> int"""
    frases_separadas=texto.split('. ') or frases_separadas=texto.split('! ') or frases_separadas=texto.split('? ')
    return len(frases_separadas)