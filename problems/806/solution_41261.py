#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x1a, y1a, x2a, y2a = ret1
    x1b, y1b,  x2b, y2b = ret2

# segunda etapa - calculo do resultado
	if x2b < x1a or x2a < x1b:
        xok = True
    else:
        xok = False
    if y2b < y1a or y2a < y1b:
        yok = True
    else:
        yok = False
    
    if xok or yok:
        return False
    else:
        return True