def colisao(ret1,ret2):
    retA=x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1
    retB=x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2
    if retA in retB:
        return True
    else:
        return False