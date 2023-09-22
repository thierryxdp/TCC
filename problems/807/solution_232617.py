def conta_frases(txt):
    """Função que conta e retorna o número de frases que aparecem no
    texto dado como argumento;
    str -> int"""
    ls = str.split(txt,".")
    l = list.remove(ls,-1)
    return len(l)