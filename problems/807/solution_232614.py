def conta_frases(txt):
    """Função que conta e retorna o número de frases que aparecem no
    texto dado como argumento;
    str -> int"""
    l = str.split(txt,".")
    return len(l)