def conta_frases(texto):
    """retorna a quantidade de frases em um texto de entrada
    string -> int"""
    x = texto.split('. ') and texto.split('! ')
    return len(x)