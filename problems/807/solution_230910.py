def conta_frases(texto):
    """retorna quantas frases existem em um texto de entrada
    string -> int"""
    x = texto.split("!","?")
    return len(x)