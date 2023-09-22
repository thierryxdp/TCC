def colchao (medidas,H,L):
    '''Função para saber se o colchão novo passará pela porta dadas as suas dimensões H e L
    int,int,int -> bool'''
    
    x = medidas[0] <= L and medidas [1]<= H
    return x