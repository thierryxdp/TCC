def colchao(medidas,H,L):
    """verifica se o colchao passa pela porta,
    se passar retorna True, caso contrário retorna False;
    list(float,float,float),float,float->bool"""
    if medidas[0]>H and medidas[1]>H and medidas[2]>H and
    medidas[0]>L or medidas[1]>L  medidas[2]>L:
        return False
    else:
        return True