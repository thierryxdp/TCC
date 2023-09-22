def colchao(medidas, H, L):
    '''
    funcao que recebe as medidas de um colchao em centimetro
    (A, B e C, sendo A<B<C) e verifica se ele passa pela porta
    de altura H e largura L
    :param medidas: list 
    :param H: int 
    :param L: int 
    :return: bool 
    '''
    [A, B, C] = medidas
    A<B<C
    if B > H and C > L:
        return False
    else:
        return True