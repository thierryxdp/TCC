def colisao(ret1,ret2):
    '''A funcao recebe duas tuplas, com quatro valores inteiros cada, que indica as coordenadas
    dos vertices inferior esquerdo e superior esquerdo do primeiro e do segundo retangulo, respectivamente.
    Retorna True caso haja colisão e False se não houver.
    tuple, tuple -> bool'''

    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    if x_sup_dir1<x_inf_esq2:
        return False
    elif x_sup_dir2<x_inf_esq1:
        return False
    elif y_sup_dir1<y_inf_esq2:
        return False
    elif y_sup_dir2<y_inf_esq1:
        return False
    else:
        return True