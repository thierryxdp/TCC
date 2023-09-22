def colisao(ret1, ret2):

    # ret1 = (x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1)
    # ret2 = (x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2)

    # Primeiro parentese: colisao no x
    # Segundo parentese: colisao no y

    if (ret1[0] <= ret2[2] and ret2[0] <= ret1[2]) and (ret1[1] <= ret2[3] and ret2[1] <= ret1[3]):
        return True
    else:
        return False