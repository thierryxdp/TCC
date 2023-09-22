def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma
     tuple, tuple --> bool'''
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if x_sup_dir2<x_inf_esq1 or x_sup_dir1<x_inf_esq2:
    x == True
    else:
    x == False
    if y_sup_dir2<y_inf_esq1 or y_sup_dir1<y_inf_esq1:
    y == True
    else:
    y == False
    if x or y:
    return False
    else:
    return True