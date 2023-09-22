def freq_palavras(frases):
    """str -> dict"""
    """retorna um dicionário com todas as frequências de casa palavra"""
    
    C = str.split(frases)
    D = []
    for c in C:
        q = str.count(frases,c)
        list.append(D,(c,q))
        pass
    return dict(D)