#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    xb1, yb1, xc1, yc1 = ret1
    xb2, yb2,  xc2, yc2 = ret2

# segunda etapa - calculo do resultado
    if xb1 <= xc2 and yb1 <= yc2:
        return True
    if xc1 >= xb2 and yc1 >= yb2:
        return True
    if xb1 >= xc2 and yb1 >= uc2:
        return True
    if xc1 <= xb2 and yc1 <= yb2:
        return True
    if
    else:
        return False