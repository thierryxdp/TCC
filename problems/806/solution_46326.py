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
    meio5=(y21-x21)/2
	meio6=(x22-x21)/2
    meio7=(y22-x22)/2
    meio8=(y22-y21)/2
    
    if x12<=meio5<=y12:
        return (True)
    if y11<=meio6<=y12:
        return (True)
    if x11<=meio7<=y11:
        return (True)
	if x11<=meio8<=x12:
    	return (True)
    else:
        return (False)