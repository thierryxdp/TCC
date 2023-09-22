def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x1e, y1e, x1d, y1d = ret1
    x2e, y2e, x2d, y2d = ret2

# segunda etapa - calculo do resultado
	if (x2e<x1d):
        return ((y2e - y1d)>=0)
    else:
        return (x2d-x1e)>=0