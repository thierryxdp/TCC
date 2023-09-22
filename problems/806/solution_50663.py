def colisao(ret1,ret2):
    '''Função colisao que recebe duas tuplas com quatro valores inteiros cada uma,
    representando as coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo retângulo,
    nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
    tuple, tuple --> bool'''

    retA1= ret1
    x_inf_esq1= retA1[0]
    y_inf_esq1= retA1[1]
    x_sup_dir1= retA1[2]
    y_sup_dir1= retA1[3]

    retA2= ret2
    x_inf_esq2= retA2[0]
    y_inf_esq2= retA2[1]
    x_sup_dir2= retA2[2]
    y_sup_dir2= retA2[3]

    return not((x_sup_dir1 < x_inf_esq2) or (x_sup_dir2 < x_inf_esq1) or (y_sup_dir1 < y_inf_esq2) or (y_sup_dir2 < y_inf_esq1))