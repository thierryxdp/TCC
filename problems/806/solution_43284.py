def colisao(ret1,ret2):
	x_inf_esq1 = ret1[0]
    x_sup_dir1 = ret1[2]
	y_inf_esq1 = ret1[1]
    y_sup_dir1 = ret1[3]
    
    x_inf_esq2 = ret1[0]
    x_sup_dir2 = ret1[2]
	y_inf_esq2 = ret1[1]
    y_sup_dir2 = ret1[3]
    if x_inf_esq1 == x_inf_esq2:
        return True
    if x_inf_esq2 == x_inf_esq1:
        return True
    else:
        return False