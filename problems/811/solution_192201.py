def colchao( medidas, H, L):
    '''
    tres dimensoes de um colchao, verifica se o colchao passa pela altura e largura da porta
    :param medidas: list->list
    :param H: int->int
    :param L: int->int
    :return: bool->bool
    '''
    [A,B,C]= medidas
    if A and B > H and L:
        return False
    
    else:
        return True