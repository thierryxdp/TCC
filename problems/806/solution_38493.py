def ret1(x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1):
    return tuple(x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1)

def ret2(x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2):
    return tuple(x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2)

def colisao(ret1,ret2):
    if ret1[0] == ret2[0] and ret1[1]>ret2[1] and ret1[2]>ret2[2] and ret1[3]>ret2[3]:
        return True
    
    if ret1[0]>ret2[0] and ret1[1]>ret2[1] and ret1[2] == ret2[2] and ret1[3]>ret2[3]:
        return True
    
    if ret1[0]<ret2[0] and ret[1]>ret2[1] and ret1[2]<ret2[2] and ret1[3]<ret1[3]:
        return True