def conta_frases(txt):
    """Função que conta e retorna o número de frases que aparecem no
    texto dado como argumento;
    str -> int"""
    l1 = str.split(txt,".")
    l2 = str.strip(l1,".")
    return len(l2)