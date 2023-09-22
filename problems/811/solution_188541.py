def colchao(medidas,H,L):
    '''Função que, dada as medidas do colchão e da porta
    responde 'True' no caso do colchão conseguir passar
    pela porta, e 'False' no caso contrário.
    
    :param medidas, H, L: list
    :return: bool
    '''
    if medidas[1:] < H,L:
        return True