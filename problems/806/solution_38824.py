#Start your python function here
def colisao(posicaoret1,posicaoret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xInfEsq1 = posicaoret1[0]
    yInfEsq1 = posicaoret1[1]
    xSupDir1 = posicaoret1[2]
    ySupDir1 = posicaoret1[3]
    xInfEsq2 = posicaoret2[0]
    yInfEsq2 = posicaoret2[1]
    xSupDir2 = posicaoret2[2]
    ySupDir2 = posicaoret2[3]
    
    houve_colisao = not(xSupDir2 < xInfEsq1 or xSupDir1 < xInfEsq2) or not (ySupDir2 < yInfEsq1 or ySupDir1 < yInfEsq2)
    
    return houve_colisao