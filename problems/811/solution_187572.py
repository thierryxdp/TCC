def colchao(medidas,H,L):
    """verifica se o colchao passa pela porta,
    se passar retorna True, caso contrário retorna False;
    list(float,float,float),float,float->bool"""
    if medidas[1]>H and medidas[1]>H:
        return False
    if medidas[2]>H and medidas[2]>L:
        return False
    else:
        return True