def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    if not('X_sup_dir2' < 'X_inf_esq1')or('X_sup_dir1' < 'X_inf_esq2')and not('Y_sup_dir2' < 'Y_inf_esq1')or('Y_sup_dir' < 'Y_inf_esq2'):
        return (True caso haja intersecao ou False caso nao haja)