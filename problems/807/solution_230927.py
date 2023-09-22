def conta_frases(texto):
    """retorna a quantidade de frases em um texto de entrada
    string -> int"""
    x = texto.split('. '), texto.split('! '), texto.split('? ')
    return len(x)