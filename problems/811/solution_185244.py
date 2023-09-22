def colchao(medidas,H,L):
    '''dadas as medidas de um colchao e da porta, retorna se o colchao passara ou nao pela porta
    lista,int,int -> bool'''
    a = medidas[0]
    b = medidas[1]
    
    if (a <= H and b <= L) or (b <= H and a <= L):
        return True
    else:
        return False