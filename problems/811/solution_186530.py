def colchao(medidas,H,L):
    '''funçao que retorna a confirmação de se o colchão passa pela prta com base nas medidas de entrada'''
    '''list,int,int->bool'''
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