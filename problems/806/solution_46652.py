def colisao(ret1,ret2):
    '''Recebe duas tuplas com quatro valores inteiros cada uma,
    representando as coordenadas do primeiro retângulo e do segundo.
    Retorna se os retângulos colidem ou não.
    tuple,tuple -> bool'''
    ret1= A1[0],A1[1],A1[2],A1[3]
    ret2= A2[0],A2[1],A2[2],A2[3]
    if A2[0] > A1[2] or A2[2] < A1[0] or A1[3] < A2[1] or A1[1] > A2[3]:
        return False
    else:
        return True