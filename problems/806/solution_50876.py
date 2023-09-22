#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
		if (x inf esql >= x inf esq2 and x inf esql <= x sup dir2) or (x sup diril >= x inf esq2 and x sup dirl <= x sup dir2):
            if (y inf esq1l >= y inf esq2 and y inf esql <= y sup dir2) or (y sup dir1il >=y inf esq2 and y sup dirl <= y sup dir2):
        		resultado = True

	return resultado