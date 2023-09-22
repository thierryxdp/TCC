def conta_frase(texto):
    """Função que, dado um texto, conta o numero de frazes que ele possui
    str -> int"""
    s = texto
    return len(s.partition(".", "!")