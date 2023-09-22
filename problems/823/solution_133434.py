def faltante(l):
    """Dada uma lista com N − 1 inteiros numerados de 1 a N,
    retorna o número inteiro deste intervalo está faltando.
    list > int"""
    x = 1
    lx = []
    while x <= len(l)+1: 
    	lx.append(x)
        x += 1
    i = 0
    if lx[-1] != l[-1]:
        return lx[-1]
    while i < len(l):
        if lx[i] != l[i]:
            return lx[i]
        i += 1