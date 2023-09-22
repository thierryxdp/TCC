#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
   [0,1,2,3]  = ret1
   [4,5,6,7]  = ret2

# segunda etapa - calculo do resultado
    if ret1[3] < ret2[5] or ret2[7] < ret1[1] \
    or ret1[4] < ret2[3] or ret2[8]< ret1[2]:
        return False
    else:
        return True