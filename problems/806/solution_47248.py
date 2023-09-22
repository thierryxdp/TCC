def colisao(ret1,ret2):
    x_inf_esq1 = ret1[0]
    y_inf_esq1 = ret1[1]
    x_sup_dir1 = ret1[2]
    y_sup_dir1 = ret1[3]
    x_inf_esq2 = ret2[0]
    y_inf_esq2 = ret2[1]
    x_sup_dir2 = ret2[2]
    y_sup_dir2 = ret2[3]

    if x_sup_dir1 < x_inf_esq2:
        return False
    elif x_sup_dir2 < x_inf_esq1:
        return False
    elif y_sup_dir1 < y_inf_esq2:
        return False
    elif y_sup_dir2 < y_inf_esq1:
        return False
    else:
        return True