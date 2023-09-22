def conta_frases(txt):
    """Função que conta e retorna o número de frases que aparecem no
    texto dado como argumento;
    str -> int"""
    ls = str.split(txt,".")
    return len(ls)