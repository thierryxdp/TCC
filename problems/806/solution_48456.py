def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xinfesq1=ret1[0]
    yinfesq1=ret1[1]
    xsupdir1=ret1[2]
    ysupdir1=ret1[3]
    xinfesq2=ret2[0]
    yinfesq2=ret2[1]
    xsupdir2=ret2[2]
    ysupdir2=ret2[3]
    if (xsupdir1 < xinfesq2) or (xsupdir2 < xinfesq1) or (ysupdir1 < yinfesq2) or (ysupdir2 < xsupdir2) or (xinfesq2 > xsupdir1) or (yinfesq1 > ysupdir2) or (yinfesq2 > ysupdir1):
        return True
    else: 
  		return False

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    #x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    #x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado