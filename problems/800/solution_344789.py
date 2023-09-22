def total(Lc,Pd):
    """list,dict -> float"""
    """retorna o preço da lista de compras"""
    
    s = 0
    for i in Lc:
        s += Pd[i]
        pass
    return round(s,2)