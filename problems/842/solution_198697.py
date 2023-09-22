def pontos_por_time(l):
    timeA=l[0][0]
    timeB=l[0][1]
    gAj1=l[0][2][0]
    gBj1=l[0][2][1]
    gAj2=l[1][2][1]
    gBj2=l[1][2][0]
    pontosA=0
    pontosB=0
    dicionario=dict()
    if gAj1>gBj1 and gAj2>gBj2:
        dicionario[timeA]=pontosA+6
        dicionario[timeB]=pontosB+0
        #return dicionario
    if gAj1>gBj1 and gAj2=gBj2:
        dicionario[timeA]=pontosA+4
        dicionario[timeB]=pontosB+1
        #return dicionario
    if gAj1=gBj1 and gAj2>gBj2:
        dicionario[timeA]=pontosA+4
        dicionario[timeB]=pontosB+1
        return dicionario
    if gAj1=gBj1 and gAj2=gBj2:
        dicionario[timeA]=pontosA+2
        dicionario[timeB]=pontosB+2
        #return dicionario
    if gAj1<gBj1 and gAj2<gBj2:
        dicionario[timeA]=pontosA+0
        dicionario[timeB]=pontosB+6
        #return dicionario
    if gAj1<gBj1 and gAj2=gBj2:
        dicionario[timeA]=pontosA+1
        dicionario[timeB]=pontosB+4
        #return dicionario
    if gAj=gBj1 and gAj2<gBj2:
        dicionario[timeA]=pontosA+1
        dicionario[timeB]=pontosB+4
        #return dicionario
    if gAj1>gBj1 and gAj2<gBj2:
        dicionario[timeA]=pontosA+3
        dicionario[timeB]=pontosB+3
        #return dicionario