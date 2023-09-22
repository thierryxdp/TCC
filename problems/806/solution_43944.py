def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior direito do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    
# segunda etapa - calculo do resultado
	if (x_sup_dir1 in (x_inf_esq2, x_sup_dir2) and y_sup_dir1 in (y_inf_esq2, y_sup_dir2)):
        return True
    
    elif (x_inf_esq1 in (x_inf_esq2, x_sup_dir2) and y_inf_esq1 in (y_inf_esq2, y_sup_dir2)):
        return  True
    
    elif (x_sup_dir2 in (x_inf_esq1, x_sup_dir1) and y_sup_dir2 in (y_inf_esq1, y_sup_dir1)):
        return True
    
    elif (x_inf_esq2 in (x_inf_esq1, x_sup_dir1) and y_inf_esq2 in (y_inf_esq1, y_sup_dir1)):
    	return True
    
   
    else:
        return False