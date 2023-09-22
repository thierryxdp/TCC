def colchao(medidas,H,L):
    a,b,c=medidas
    L = int(H)
    H = int(L)
    a = int(a)
    b = int(b)
    c = int(c)
    if (a,b,c) > (H,L):
        return (False)
    else:
        return(True)