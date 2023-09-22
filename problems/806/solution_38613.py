def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    x_inf_esq1=ret1[0]
    y_inf_esq1=ret2[0]
    x_sup_dir1=ret1[1]
    y_sup_dir1=ret2[1]
    x_inf_esq2=ret1[2]
    y_inf_esq2=ret2[2]
    x_sup_dir2=ret1[3]
    y_sup_dir2=ret2[3]
    xyInfEsq1= y_inf_esq1-(x_inf_esq1)
    xySupDir1=y_sup_dir1-(x_sup_dir1)
    xyInfEsq2=y_inf_esq2-(x_inf_esq2)
    xySupDir2=y_sup_dir2-(x_sup_dir2)
    
    if xyInfEsq1!=0 or xySupDir1!=0:
      return True
    if xyInfEsq2!=0 or xySupDir2!=0:
        return True
    if xyInfEsq1==0 and xySuprDir1==0:
      return False
    if xyInfEsq2==0 and xySupDir2==0:
      return False