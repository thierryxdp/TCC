def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2 = ret2

	ax1, ay1 = x_inf_esq1, y_inf_esq1
    ax2, ay2 = x_sup_dir1, y_inf_esq1
    ax3, ay3 = x_sup_dir1, y_sup_dir1
    ax4, ay4 = x_inf_esq1, y_sup_dir1
    
    bx1, by1 = x_inf_esq2, y_inf_esq2
    bx2, by2 = x_sup_dir2, y_inf_esq2
    bx3, by3 = x_sup_dir2, y_sup_dir2
    bx4, by4 = x_inf_esq2, y_sup_dir2
    
    
# segunda etapa - cálculo do resultado
	if ax1 == bx1 and ay1 == by1 or ax1 == bx2 and ay1 == by2
    	return True
    
    elif ax2 == bx1 and ay2 == by1 or ax2 == bx2 and ay2 == by2
    	return True
    
    elif ax3 == bx1 and ay3 == by1 or ax3 == bx2 and ay3 == by2 or ax3 == bx3 and
    	return True
    
    elif ax4 == bx1 and ay4 == by1 or ax4 == bx2 and ay4 == by2 or ax4 == bx3 and
    	return True
    
    elif bx1 < ax1 < bx2 and by1 < ay1 < by2 or bx2 < ax1 < bx3 and by2 < ay1 <
    	return True
    
    elif bx1 < ax2 < bx2 and by1 < ay2 < by2 or bx2 < ax2 < bx3 and by2 < ay2 <
    	return True
    
    elif bx1 < ax2 < bx2 and by1 < ay2 < by2 or bx2 < ax2 < bx3 and by2 < ay2 <
    	return True
    
    elif bx1 < ax4 < bx2 and by1 < ay4 < by2 or bx2 < ax4 < bx3 and by2 < ay4 <
    	return True
    
    else:
        return False