#Start your python function here
def colisao(ret1,ret2):
        '''
    a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
    coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
    retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
    
    x1 = coord. x do vertice inferior da diagonal do retangulo 1
    y1 = coord. y do vertice inferior da diagonal do retangulo 1
    x2 = coord. x do vertice superior da diagonal do retangulo 1
    y2 = coord. y do vertice superior da diagonal do retangulo 1
    x3 = coord. x do vertice inferior da diagonal do retangulo 2
    y3 = coord. y do vertice inferior da diagonal do retangulo 2
    x4 = coord. x do vertice superior da diagonal do retangulo 2
    y4 = coord. y do vertice superior da diagonal do retangulo 2
    tupla, tupla --> bool
    '''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x1, y1, x2, y2 = figura_1
    x3, y3, x4, y4 = figura_2

# segunda etapa - calculo do resultado
	if x2<x3:
        return False
    elif x4<x1:
		return False
    elif y2<y3:
    	return False
    elif y4<y1:
    	return False
    else:
    	return True