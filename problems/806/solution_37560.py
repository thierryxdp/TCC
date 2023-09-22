def colisao (ret1, ret2):
    '''Calcula e retorna "True" se há colisão e "False", caso contrário em base das tuplas "ret1" e "ret2" formadas por quatro valores inteiros cada uma,
    representando as coordenadas dos vértices inferior esquerdo e superior direito do primeiro retângulo e do segundo retângulo, nessa ordem;
    tuple, tuple -> bool'''
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    
    if ret1[0] > ret2[0]:
        if ret2[0] > ret1[0]:
            pass
        else:
            return True
    elif ret1[0] < ret2[0]:
        if ret1[0] > ret2[0]:
            pass
        else:
            return True
    elif ret1[0] == ret2[0]:
        return True
            
    elif ret1[1] > ret2[1]:
        if ret2[1] > ret1[1]:
            pass
        else:
            return True
    elif ret1[1] == ret2[1]:
        return True
    else:
        return False