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
    meiox1=(x11-x12)/2
    meiox2=(x22-y22)/2
    meioy1=(x11-y11)/2
    meioy2=(y21-y22)/2
    
    if x11<=meiox1<=x12 or x21<=meiox2<=y22 or x11<=meioy1<=y11 or y22<=meioy2<=y22:
        return (True)
    else:
        return (False)