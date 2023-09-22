def colchao (medidas,H,L):
    '''Função para saber se o colchão novo passará pela porta dadas as suas dimensões H e L
    int,int,int -> bool'''
    
    if H>L:
        x = medidas[0] <= L and medidas [1]<= H
        return x
    else:
        x = medidas[0] <= H and medidas [1]<= L
        return x