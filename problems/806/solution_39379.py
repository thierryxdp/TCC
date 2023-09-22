def colisao(ret1,ret2):
    """Funcao que dado 2 retangulos, determina se havera colisao entre eles"""
    ret1= x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1
    ret2= x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2
    if y_inf_esq1 <= x_sup_dir1:
        return True
    else:
        return False