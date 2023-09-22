def colchao(medidas,H,L):
    '''funçao que calcula se o colchao passa na porta da casa de joao,dado as medidas do colchao e das portas; lista,int,int -> bool'''
    if medidas[:1] <= L and medidas[2:] <= H:
        return True
    elif medidas[1:2] <= L and medidas[2:] <= H:
        return True
    elif medidas[2:] <= L and medidas[1:2] <= H:
        return True
    else
        return False