def posLetra(p,l,n):
    i = 0
    cont = 0
    if str.counte(p,l) < n:
        return -1
    else:
        while i < len(p):
        qtdL = str.fid(p,l,i)