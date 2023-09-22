#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    from math import *

    Uso:
    colisao(reta1,reta2)

    Entrada:
    - reta1 (tupla, obrigatorio): x1,y1,x2,y2
    - reta2 (tupla, obrigatorio): x3,y3,x4,y4

    Saida:
    - Retorna True se ha colisao entre os 2 retangulos ou False caso contrario. (booleana)
     '''
    
    x1,y1,x2,y2 = reta1
    x3,y3,x4,y4 = reta2

    if x2<x3 or x4<x1 or y2<y3 or y4<y1:
        return False
    else:
        return Tru

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado