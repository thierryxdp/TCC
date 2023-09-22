def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    inf_esq1, inf_dir1, sup_esq1, sup_dir1 = ret1
    inf_esq2, inf_dir2, sup_esq2, sup_dir2 = ret2
    
    if (inf_esq1 >= sup_dir2) or (inf_esq2 >= sup_dir1):
        return True
    else:
        return False