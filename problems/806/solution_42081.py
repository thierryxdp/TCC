def colisao(ret1,ret2):
    '''
    Detecta se há colisão entre doi retângulos.
    tuple, tuple --> bool
    '''
    x_inf_esq1=ret1[0]
    y_inf_esq1=ret1[1]
    x_sup_dir1=ret1[2]
    y_sup_dir1=ret1[3]
    x_inf_esq2=ret2[0]
    y_inf_esq2=ret2[1]
    x_sup_dir2=ret2[2]
    y_sup_dir2=ret2[3]
    v1_ret1=(x_sup_dir1,y_inf_esq1)
    v2_ret1=(x_sup_dir1,y_sup_dir1)
    v3_ret1=(x_inf_esq1,y_inf_esq1)
    v4_ret1=(x_inf_esq1,y_sup_dir1)
    v1_ret2=(x_sup_dir2,y_inf_esq2)
    v2_ret2=(x_sup_dir2,y_sup_dir2)
    v3_ret2=(x_inf_esq2,y_inf_esq2)
    v4_ret2=(x_inf_esq2,y_sup_dir2)
    if v1_ret1==v1_ret2 or v1_ret1==v2_ret2 or v1_ret1==v3_ret2 or v1_ret1==v4_ret2:
        return True
    elif v2_ret1==v1_ret2 or v1_ret1==v2_ret2 or v1_ret1==v3_ret2 or v1_ret1==v4_ret2:
        return True
    elif v3_ret1==v1_ret2 or v1_ret1==v2_ret2 or v1_ret1==v3_ret2 or v1_ret1==v4_ret2:
        return True
    elif v4_ret1==v1_ret2 or v1_ret1==v2_ret2 or v1_ret1==v3_ret2 or v1_ret1==v4_ret2:
        return True
    else:
        return False