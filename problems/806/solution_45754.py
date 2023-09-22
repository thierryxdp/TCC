#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    xif1, yif1, xsd1, ysd1 = ret1
    xif2, yif2, xsd2, ysd2 = ret2

# segunda etapa - calculo do resultado
	if ((xif2 < xif1) and (yif1 < yif2)):
        return True
   	elif ((xif1 < xsd2) and (yif1 < ysd2)):
        return True
    else:
        return False
	#if ((xif2 < xif1) and (yif1 < yif2)) and ((xif1 < xsd2) and (yif1 < ysd2)):
    #    return True
   	#else:
    #    return False