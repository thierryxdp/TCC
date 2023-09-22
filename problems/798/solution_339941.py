def ⁷freq_palavras(frases):
    """str -> dict"""
    """retorna um dicionário com a frequência de cada palavra no texto"""
    
    C = str.split(frases)
    C.reverse()
    D = []
    
    for c in C:
        q = C.count(c)
        list.append(D,(c,q))
        pass
    R = dict(D)
    return R