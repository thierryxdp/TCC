def colisao(ret1,ret2):
    x_esq1, y_inf1, x_dir1, y_sup1 = ret1
    x_esq2, y_inf2, x_dir2, y_sup2 = ret2
    if x_dir2 < x_esq1 or x_dir1 < x_esq2:
        return False
    if y_sup2 < y_inf1 or y_sup1 < y_inf2:
        return False
    return True