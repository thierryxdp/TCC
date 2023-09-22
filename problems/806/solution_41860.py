def cria_ret(x0,y0,x1,y1):
    return(x0,y0,x1,y1)

	ret1 = cria_ret1(0,0,1,1)
    ret2 = cria_ret2(1,1,2,2)
    
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x0_ret1, y0_ret1, x1_ret1, y1_ret1 = ret1
    x0_ret2, y0_ret2, x1_ret2, y1_ret2 = ret2

# segunda etapa - calculo do resultado
	if (x0_ret1 == x0_ret2 and y0_ret1 == y0_ret2) or (x0_ret1 == x1_ret2 and y0_ret1 == y1_ret2):
    	return 'True'
    elif (x1_ret1 == x0_ret2 and y1_ret1 == y0_ret2) or (x1_ret1 == x1_ret2 and y1_ret1 == y1_ret2):
		return 'False'
    else:
        return 'True'