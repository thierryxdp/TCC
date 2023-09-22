def colchao(medidas,H,L):
    """Dadas as medidas AxBXC (A<B<C) de um colchão retorna True se o colchão passa pela porta de altura H e comprimento L, e false caso contrário.
    list, int,int->bool"""
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    
    return B>H