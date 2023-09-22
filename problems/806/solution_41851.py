#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    if [(ret1[1]>ret2[1] and ret1[1]<ret2[3]) and (ret2[1]>ret1[1] and ret2[1]<ret1[3])] and [(ret2[0]<ret1[0] and ret1[0]<ret2[2])or(ret1[0]<ret2[0] and ret2[0]<ret1[2])]:
     return True
    else:
     return False    
# segunda etapa - calculo do resultado