def colisao(ret1,ret2):
    ret1 = xi_e1, ys_e1, xi_d1, ys_d1 
    ret2 = xi_e2, ys_e2,  xi_d2, ys_d2
    if xi_d1<xi_e2:
        return False
    elif xi_d2<xi_e1:
        return False
    elif ys_e1<ys_e2 and ys_d1<ys_d2:
        return False
    elif ys_e2<ys_e1 and ys_d2<ys_d1:
        return False
    else:
        return True