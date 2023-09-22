import math
#Start your python function here
def colisao(ret1,ret2):
    r1=((ret1[0],ret1[1]),(ret1[0],ret1[3]),(ret1[2],ret1[3]),(ret1[2],ret1[1]))
    r2=((ret2[0],ret2[1]),(ret2[0],ret2[3]),(ret2[2],ret2[3]),(ret2[2],ret2[1]))
    
    if r1[0] in r2 or r1[1] in r2 or r1[2] in r2 or r1[3] in r2:
        return True
    elif r2[0] in r1 or r2[1] in r1 or r2[2] in r1 or r2[3] in r1:
        return True
    elif r2[2]<r1[2]:
        return True
    else:
        return False

    
    
    
    
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado