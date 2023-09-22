def colisao(ret1,ret2):
    """A função recebe duas tuplas com quatro valores
    inteiros cada uma, rep, tuple, tuple --> bool"""
    
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2 = ret2
    if not (x_sup_dir2 < x_inf_esq1 or x_sup_dir1 < x_inf_esq2) and not (y_sup_dir2)
    return true
else:
    return false