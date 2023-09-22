def colisao(ret1,ret2):
	x_inf_esq1 = ret1[0]
    x_sup_dir1 = ret1[2]
	y_inf_esq1 = ret1[1]
    y_sup_dir1 = ret1[3]
    
    x_inf_esq2 = ret1[0]
    x_sup_dir2 = ret1[2]
	y_inf_esq2 = ret1[1]
    y_sup_dir2 = ret1[3]
    reta = x_inf_esq1 + x_sup_dir1 
    reta2 = x_inf_esq2 + x_sup_dir2
    if reta != reta2:
        return True
    if reta != reta2:
        return True
    else:
        return False
        return False