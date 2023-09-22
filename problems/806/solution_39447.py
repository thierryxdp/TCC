def colisao(ret1,ret2):
    '''
    '''

    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2 = ret2

    if (ret1[1]<ret2[0] and ret1[2]>ret1[0]):
        return False

    else ret2[1]<ret1[0] and ret2[2]>ret2[0]:
        return False