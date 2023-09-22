def colisao(ret1,ret2):
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2	
	if ret1[3:]==ret[3:]:
        return True
    if len(ret2[3:])-len(ret1[3:])==1:
        return True
    if len(ret2[3:])-len(ret1[3:])>1:
        	return False