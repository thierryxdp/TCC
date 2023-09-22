def colisao(ret1, ret2):
    '''Recebe duas tuplas com quatro valores inteiros
    cada uma, representando as coordenadas dos vértices
    inferior esquerdo e superior direito do primeiro
    retângulo e do segundo retângulo, nessa ordem, e
    devolve True se há colisão entre os 2 retângulos e
    False, caso contrário
    tuple, tuple -> bool'''
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    ver_colisao = False

    if x_sup_dir1 == x_inf_esq2:
        if y_sup_dir1 <= y_sup_dir2 and y_sup_dir1 >= y_inf_esq2:
            ver_colisao = True
        elif y_inf_esq1 <= y_sup_dir2 and y_inf_esq1 >= y_inf_esq2:
            ver_colisao = True

    if x_sup_dir2 == x_inf_esq1:
        if y_sup_dir2 <= y_sup_dir1 and y_sup_dir2 >= y_inf_esq1:
            ver_colisao = True
        elif y_inf_esq2 <= y_sup_dir1 and y_inf_esq2 >= y_inf_esq1:
            ver_colisao = True

    if y_sup_dir1 == y_inf_esq2:
        if x_sup_dir1 <= x_sup_dir2 and x_sup_dir1 >= x_inf_esq2:
            ver_colisao = True
        elif x_inf_esq1 <= x_sup_dir2 and x_inf_esq1 >= x_inf_esq2:
            ver_colisao = True
            
    if y_sup_dir2 == y_inf_esq1:
        if x_sup_dir2 <= x_sup_dir1 and x_sup_dir2 >= x_inf_esq1:
            ver_colisao = True
        elif x_inf_esq2 <= x_sup_dir1 and x_inf_esq2 >= x_inf_esq1:
            ver_colisao = True

    return ver_colisao