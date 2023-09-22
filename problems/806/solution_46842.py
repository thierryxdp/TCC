#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    
    x_inf_esq1=a
    x_inf_esq2=e
	y_inf_esq1=b
    y_inf_esq2=f
    x_sup_esq1=c
    x_sup_esq2=g
	y_sup_esq1=d
    y_sup_esq2=h
    
    if a >= e or a >= f or a >= g or a >= h or b >= e or b >= f or b >= g or b >= h or c >= e or c >= f or c >= g or c >= h d >= e or d >= f or d >= g or d >= h    
        return True
    else:
        return False
# segunda etapa - calculo do resultado