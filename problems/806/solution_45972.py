def colisao(ret1,ret2):
    '''
    Funcao que retorna se dois triangulos se interceptam ou não.
    tupla, tupla -> booleano
    '''
    (x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1)=ret1
    (x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2)=ret2
    if (ret1[2]<ret2[0] or ret2[2]<ret1[0]) or (ret1[3]<ret2[1] or ret2[3]<ret1[1]):
        return False
    else:
        return True