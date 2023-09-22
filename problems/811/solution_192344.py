def colchao (medidas, H, L):
    '''Função que observa se um colchão consegue passar pelas portas
    int, int, int -> bool'''
    # H = altura, L = largura
    
    return (medidas[0]<=L and medidas [1]<=H) or (medidas[0]<=H and medidas[1]<=L)