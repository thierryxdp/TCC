def colisao(ret1:tuple,ret2:tuple)->bool:
    '''Recebe duas tuplas com quatro valores inteiros cada uma,
    representando as coordenadas do primeiro retângulo e do segundo.
    Retorna se os retângulos colidem ou não.
    tuple,tuple -> bool'''
    if ret2[0] > ret1[2] or ret2[2] < ret1[0] or ret1[3] < ret2[1] or ret1[1] > ret2[3]:
        return False
    else:
        return True