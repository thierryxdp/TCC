def colchao(medidas, H, L):
    ''' Verifica se o colchão passa através das portas da casa.
    	list, int, int -> bool
        
    	Parameters:
        medidas: Lista contendo as dimensões do colchão.
        H: Altura das portas.
        L: Largura das portas.
        
        Returns:
        True se o colchão passa pelas portas, e False caso contrário.
    '''
    if medidas[1] <= H:
        return True
    elif medidas[1] > H:
        return False