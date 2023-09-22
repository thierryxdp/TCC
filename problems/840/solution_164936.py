def bolos(nXicarasFarinha,nOvos,nColheresLeite):
    maxFarinha = nXicarasFarinha//2
    maxOvos = nOvos//3
    maxLeite = nColheresLeite//5
    if maxFarinha <= maxOvos:
        if maxLeite <= maxFarinha:
            return maxLeite
        else:
            return maxFarinha
    else:
        if maxLeite <= maxOvos:
            return maxLeite
        else:
            return maxOvos