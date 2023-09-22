#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
  xinfe1, yinfe1, xsup1, ysup1 = ret1
  xinfe2, yinfe2, xsup2, ysup2 = ret2

# segunda etapa - calculo do resultado
    if xsup1 < xinfe2 or xsup2 < xinfe1 or ysup1 < yinfe2 or ysup2 < yinfe1:
       return False
    else :
        return True