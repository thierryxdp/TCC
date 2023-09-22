def colisao(ret1,ret2):
    ''' função que dadas duas tuplas (ret1 e ret2) com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior direito do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se há colisao entre os 2 retangulos e False, caso contrario.
     Entrada: tupla (int, int, int, int), tupla (int, int, int, int)
     Retorno: bool '''

    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    if (ret2[0]>ret1[2] or ret1[0]>ret2[2]) or (ret1[1]>ret2[3] or ret2[1]>ret1[3]):
        return False

    else:
        return True