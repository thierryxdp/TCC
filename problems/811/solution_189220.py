def colchao(medidas,H,L):
    '''esse colchão passa pela porta? (A,B,C)medidas=centímetros do colchão
H,L=centímetros da porta.
float,float,float,float,float->bool'''
    if H>=A:
        return True
    if L>=B:
        return True
    if H>=B:
        return True
    if L>=A:
        return True
    if H>=C:
        return True
    if L>=B:
        return True
    else:
        return False