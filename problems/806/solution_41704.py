#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    xie1=ret1[0]
    yie1=ret1[1]
    xsd1=ret1[2]
    ysd1=ret1[3]
    xie2=ret2[0]
    yie2=ret2[1]
    xsd2=ret2[2]
    ysd2=ret2[3]
# segunda etapa - calculo do resultado
    if xie1 > xsd2:
       return True
    else:
       return False