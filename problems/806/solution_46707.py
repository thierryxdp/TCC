#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    reta1x=ret1[0],ret1[1]
    reta1y=ret1[2],ret1[3]
    reta2x=ret2[0],ret2[1]
    reta2y=ret2[2],ret2[3]
    if reta2y>reta1y:
        if reta2x>reta1x:
            return True
    elif reta2x<reta1x:
          if reta2y<reta1y:
                return True
    else:
          return False

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado