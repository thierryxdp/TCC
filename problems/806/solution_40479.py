def colisao(ret1,ret2):
    '''Função que dado duas tuplas(ret1 e ret1) com quatro valores inteiros cada uma, representando as 
     coordenadas dos vértices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se há colisão entre os 2 retângulos e False, caso contrário.
     tuple, tuple --> bool'''

    x_inf_esq1 = ret1[0]
    y_inf_esq1 = ret1[1]
    x_sup_dir1 = ret1[2]
    y_sup_dir1 = ret1[3]
    x_inf_esq2 = ret2[0]
    y_inf_esq2 = ret2[1]
    x_sup_dir2 = ret2[2]
    y_sup_dir2 = ret2[3]

    return not (x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2) and not (y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2)