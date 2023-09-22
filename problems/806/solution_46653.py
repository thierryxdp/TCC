def colisao(ret1,ret2):
    '''Recebe duas tuplas com quatro valores inteiros cada uma,
    representando as coordenadas do primeiro retângulo e do segundo.
    Retorna se os retângulos colidem ou não.
    tuple,tuple -> bool'''
    ret1= A10, A11, A12, A13
    ret2= A20, A21, A22, A23
    if A20 > A12 or A22 < A10 or A13 < A21 or A11 > A23:
        return False
    else:
        return True