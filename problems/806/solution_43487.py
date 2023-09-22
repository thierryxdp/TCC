#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    
    # retângulo 1
    x1 = x_inf_esq1 
    y1 = y_inf_esq1
    x2 = x_sup_dir1 
    y2 = y_sup_dir1
    
    #retângulo 2
    x3 = x_inf_esq2 
    y3 = y_inf_esq2 
    x4 = x_sup_dir2
    y4 = y_sup_dir2
    
    if (x2 < x3 or x4 <x1) and (y2 < y3 or y4 <y1):
        return True
    else:
        return False
    

# segunda etapa - calculo do resultado