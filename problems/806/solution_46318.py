#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x11=ret1[0]
    y11=ret1[1]
    x12=ret1[2]
    y12=ret1[3]
    x21=ret2[0]
    y21=ret2[1]
    x22=ret2[2]
    y22=ret2[3]
# segunda etapa - calculo do resultado
    meio1=(y11-x11)/2
	meio2=(x11-x12)/2
    meio3=(y12-x12)/2
    meio4=(y12-x12)/2
    meio1=(y21-x21)/2
	meio2=(x21-x22)/2
    meio3=(y22-x22)/2
    meio4=(y22-x22)/2
    
    if x22<=meio1<=y22 or y21<=meio2<=y22 or x21<=meio3<=y21 or x21<=meio4<=x22:
        return (True)
    else:
        return (False)