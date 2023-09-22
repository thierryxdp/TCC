def colchao(medidas,H,L):
    pc,ac,lc=medidas 
    if ac/H<=1:
        return (True)
    if ac/L<=1:
        return (True)
    if ac/H>1:
        return (False)
    else:
        if ac/L<1:
            return (False)