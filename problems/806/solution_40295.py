#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
    import math
    
    def dist(p1,p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    pA1, pA2 = (x_inf_esq1, y_inf_esq1), (x_sup_dir1, y_sup_dir1)
    pB1, pB2 = (x_inf_esq2, y_inf_esq2), (x_sup_dir2, y_sup_dir2)
    
    if dist(pA1,pA2) < dist(pA1,pB1) or dist(pA1,pA2) < dist(pA1,pB2):
        return True
    else:
        return False