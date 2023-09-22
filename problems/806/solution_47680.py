def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    xie1, yie1, xsd1, ysd1 = ret1
    xie2, yie2,  xsd2, ysd2 = ret2

# segunda etapa - calculo do resultado

    if ( xie1 <= xie2 <= xsd1 or yie1 <= yie2 <= ysd1):

        return True
	
    if ( xie1 <= xsd2 <= xsd1 or yie2 <= yie1 <= ysd2):

         return True

	if (xsd2 >= xie1 >= xie2 and yie1 >= ysd2 >= ysd1):
		
		return True

		
    else: 
	
     return False