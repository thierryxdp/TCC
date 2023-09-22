def colchao(medidas, H, L):
    '''
    funcao que recebe as medidas de um colchao 
    em centimetro e verifica se ele passa pela porta
    de altura H e largura L
    lis,int,int->bool
    '''
    [A, B, C] = medidas
    A<B<C
    if B > H and C > L:
        return False
    else:
        return True