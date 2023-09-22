def pontos_por_time(lista):
    pontosA=0
    pontosB=0
    if lista[0][2][0]>lista[0][2][1]:
        pontosA=pontosA+3
    if lista[0][2][0]==lista[0][2][1]:
        pontosA=pontosA+1
        pontosB=pontosB+1
    if lista[0][2][0]<lista[0][2][1]:
        pontosB=pontosB+3
    if lista[1][2][0]<lista[1][2][1]:
        pontosA=pontosA+3
    if lista[1][2][0]==lista[1][2][1]:
        pontosA=pontosA+1
        pontosB=pontosB+1
    if lista[1][2][0]>lista[1][2][1]:
        pontosB=pontosB+3
    placar={lista[0][1]:pontosA,lista[0][2]:pontosB}
    return placar