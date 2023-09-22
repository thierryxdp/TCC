def conta_frases(texto):
    """contará o número de frases dentro de um texto
    string-->int"""
    x=str.strip(texto,"!")
    return len(x)