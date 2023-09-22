def colchao (medidas,H,L):
    '''Função para saber se o colchão novo passará pela porta
    int,int,int -> bool'''
    
    x = medidas[2] >= H and medidas [1]>= L
    return x