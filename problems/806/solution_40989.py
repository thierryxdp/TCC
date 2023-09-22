#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    xinf1, yinf1, xsup1, ysup1 = ret1[0],ret1[1],ret1[2],ret1[3]
    xinf2, yinf2,  xsup2, ysup2 = ret2[0],ret2[1],ret2[2],ret2[3]

    if(xsup2<xinf2 or xsup1 < xinf2) or (ysup2 < yinf1 or ysup1 < yinf2):
        return False
    return True