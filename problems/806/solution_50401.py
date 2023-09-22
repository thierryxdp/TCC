#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1[0][0], y_inf_esq1[0][0], x_sup_dir1[0][1], y_sup_dir1[0][1] = ret1
    x_inf_esq2[1][0], y_inf_esq2[1][0], x_sup_dir2[1][1], y_sup_dir2[1][1] = ret2
    
    #ret1 = [[0,0],[0,0]]
    #ret2 = [[0,0],[0,0]]

# segunda etapa - calculo do resultado
	for i in range(0, 2):
        for j in range(0, 2):
            ret1[i][j] = int(ret1[i][j])
            for i in range(0, 2):
                for j in range(0, 2):
                    ret2[i][j] = int(ret2[i][j])
                    
	if (ret1[0][1] > ret2[1][0]) or (ret1[1][1] < ret1[0][0]) or (ret2[0][1] < ret2[1][0]) or (ret2[1][1] < ret2[1][1]) or (ret1[1][0] > ret1[0][1]) or (ret2[0][0] > ret2[1][1]) or (ret2[1][0] > ret2[0][1]):
        return True
    else:
        return False