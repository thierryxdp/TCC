def colisao(ret1,ret2):
    if type(ret1) != tuple:
        reta = tuple(ret1)
    if type(ret2) != tuple:
        retb = tuple(ret2)
    reta = x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1
    retb= x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2
    
    if x_sup_dir1 < x_inf_esq2 or x_sup_dir2 < x_inf_esq1 or y_sup_dir1 < y_inf_esq2 or y_sup_dir2 < y_inf_esq1:
        return False
    else:
        return True