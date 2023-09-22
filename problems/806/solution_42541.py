def colisao(ret1,ret2):
    """a funcao colisao recebe duas tuplas com quatro valores cada um, os quais representam as cordenadas do vertice inferior esquerdo e do vertice superior direito do retangulo, respectivamente, e retorna True se há colisao entre os retangulos e False se nao ha colisao;
    tuple, tuple -> bool"""
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if ((x_inf_esq1<=x_inf_esq2 and x_inf_esq2<=x_sup_dir1)or(x_inf_esq1<=x_sup_dir2 and x_sup_dir2<=x_sup_dir1))and((y_inf_esq1<=y_inf_esq2 and y_inf_esq2<=y_sup_dir2)or(y_inf_esq1<=y_sup_dir2 and y_sup_dir2<=y_sup_dir1)):
        return False
    else:
        return True