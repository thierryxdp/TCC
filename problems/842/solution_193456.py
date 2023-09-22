def pontos_por_time(lista):
    '''Recebe como entrada uma lista contendo duas listas, que por sua vez tem informaçoes sobre o numero de gols de dois 
    times em dois jogos, então, calcula o a pontuação de cade time e retorna um dictionary contendo as informações sobre pontuação dos times.list->dict'''  
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
    placar={(str(lista[0][0])):pontosA,(str(lista[0][1])):pontosB}
    return placar