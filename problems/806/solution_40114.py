def colisao(ret1, ret2):
    '''A função colisão recebe duas tuplas com quatro valores inteiros cada uma, representando as coordenadas dos vértices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo retângulo, nessa ordem, e devolve True se há colisão entre os 2 retângulos e False, caso contrário; tuple, tuple -> bool.'''
    ret1 = ret1[0], ret1[1], ret1[2], ret1[3]
    ret2 = ret2[0], ret2[1], ret2[2], ret2[3]
    ret1[0], ret1[1], ret1[2], ret1[3] = x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1
    ret2[0], ret2[1], ret2[2], ret2[3] = x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2

    if (x_sup_dir1 < x_inf_esq2 or x_inf_esq1 < x_sup_dir2):
        return False
    if (y_sup_dir1 < y_inf_esq2 or y_inf_esq1 < y_sup_dir2):
        return False
    else:
        return True