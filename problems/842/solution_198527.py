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
	if gAj1>gBj1 and gAj2=gBj2:
        dicionario[timeA]=pontosA+4
        dicionario[timeB]=pontosB+1
	if gAj1=gBj1 and gAj2>gBj2:
        dicionario[timeA]=pontosA+4
        dicionario[timeB]=pontosB+1
	returndicionario