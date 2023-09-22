#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    ret1 = x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1
    ret2 = x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2
    
    s = (x_i_esq1, y_i_esq1, x_s_dir1, y_s_dir1) 
    n = (x_i_esq2, y_i_esq2, x_s_dir2, y_s_dir2)
    
    if s[2] < n[2] or n[2] < s[2] or s[3] < n[3] or n[3] < s[3]:
        return True 
    else:
        return False