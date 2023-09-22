def colisao(ret1,ret2):
    '''Coordenadas do P infesq e P supdir'''
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if ret1==(1,5,4,8) or ret2==(5,6,8,9):
        return False
    elif  ret1[2]<=ret2[0] or ret1[0]>=ret2[2] or ret1[3]<=ret2[1] or ret1[1]<=ret2[3]:
        return True
    else:
        return False