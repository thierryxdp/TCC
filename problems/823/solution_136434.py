def faltante(l):
    """"""
    list.sort(l)
    proximo = 0
    
    if 1 not in l:
        return 1
    
    else:
        while proximo < len(l):
            if l[proximo+1] != l[proximo] + 1:
                return proximo+2
        proximo = proximo + 1