def colchao(medidas,H,L):
    pc,ac,lc=medidas 
    if ac/H>=0:
        return (True)
    if ac/L>=0:
        return (True)
    if ac/H<0:
        return (False)
    else:
        if ac/L<0:
            return (False)