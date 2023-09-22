def colisao(ret1,ret2):
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

	if x_inf_esq1 > x_sup_dir2:
        return False
    if x_inf_esq2 > x_sup_dir1:
        return False
    if y_inf_esq1 > y_sup_dir2:
        return False
    if y_inf_esq2 > y_sup_dir1:
        return False
    
    return True