def colchao(medidas,H,L):
    '''esse colchão passa pela porta? (A,B,C)medidas=centímetros do colchão
H,L=centímetros da porta.
float,float,float,float,float->bool'''
    if h>=A:
        return True
    if l>=B:
        return True
    if h>=B:
        return True
    if l>=A:
        return True
    if h>=C:
        return True
    if l>=B:
        return True
    else:
        return False