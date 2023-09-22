def ret1(x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1):
    return tuple(x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1)

def ret2(x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2):
    return tuple(x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2)

def colisao(ret1,ret2):
    if ret1>=ret2:
        return True
    
    if x_inf_esq1>x_inf_esq2:
        return True