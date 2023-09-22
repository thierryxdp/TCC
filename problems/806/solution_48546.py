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
    X1 = max(x_inf_esq1,x_inf_esq2)
    X2 = min(x_sup_dir1,x_sup_dir2)
    Y1 = max(y_inf_esq1,y_inf_esq2)
    Y2 = min(y_sup_dir1,y_sup_dir2)
    
    if not(X1 >= ret1[0] and X2 <=ret1[2] and Y1 >= ret1[1] and Y2 <= ret1[3]) or (X1 > X2 or Y1 > Y2) :
        return False
    else:
        return True