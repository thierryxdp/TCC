def colisao(posicaoret1,posicaoret2):
    xInfEsq1 = posicaoret1[0]
    yInfEsq1 = posicaoret1[1]
    xSupDir1 = posicaoret1[2]
    ySupDir1 = posicaoret1[3]
    xInfEsq2 = posicaoret2[0]
    yInfEsq2 = posicaoret2[1]
    xSupDir2 = posicaoret2[2]
    ySupDir2 = posicaoret2[3]
    
    houve_colisao = not(xSupDir2 < xInfEsq1 or xSupDir1 < xInfEsq2) and not (ySupDir2 < yInfEsq1 or ySupDir1 < yInfEsq2)
    return houve_colisao