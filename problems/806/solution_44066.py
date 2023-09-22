#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    xa, ya, xb, yb = ret1
    xc, yc,  xd, yd = ret2

# segunda etapa - calculo do resultado
    Colisao= (xd<xa or xb<xc) and (yd<ya or yb<yc)
    if colisao:
        return bool(colisao)
    else:
        return False