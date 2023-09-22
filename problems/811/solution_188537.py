def colchao(medidas,H,L):
    '''Função que, dada as medidas do colchão e da porta
    responde 'True' no caso do colchão conseguir passar
    pela porta, e 'False' no caso contrário.
    
    :param medidas, H, L: list
    :return: bool
    '''
    if medidas[1]<H and medidas[2]<L:
        return True
    
    if medidas[1]<H or medidas[2]<L:
        return True
    
    elif medidas[2]<H and medidas[1]<L:
        return True
    
    elif medidas[1]>H and medidas[2]>L or medidas[2]>H and medidas[1]>L:
        return False