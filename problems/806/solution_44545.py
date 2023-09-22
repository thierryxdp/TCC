def colisao(ret1,ret2):
    """Função que recebe duas tuplas com quatro valores inteiros cada uma,
    representando as coordenadas dos vertices inferior esquerdo e superior
    esquerdo do primeiro retângulo e do segundo retângulo, nessa ordem, e
    devolve True se há colisão entre os 2 retângulos e False, caso contrario.
    tuple, tuple --> bool"""
    if ret1[2] < ret1[3] or ret1[4] < ret1[1] or ret2[2] < ret2[3] or ret2[4] < ret2[1]:
        return True 
    else:
        False