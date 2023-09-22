def colisao(ret1,ret2):
    x_inf_esq1, y_inf_dir1, x_sup_esq1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_dir2,  x_sup_esq2, y_sup_dir2 = ret2
    if  ret1[2]<=ret2[0] or ret1[0]>=ret2[2] or ret1[3]<=ret2[1] :
        return True
    else:
        return False