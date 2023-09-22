def pontos_por_time(partidas):
    'dada uma lista contendo as informacoes de duas partidas, no formato time A, time B, placar, retorna um dicionario relacionando o time e a quantidade de pontos na rodada'
    pontosA=0
    pontosB=0
    if partidas[0][2][0]>partidas[0][2][1]:
        pontosA=pontosA+3
    elif partidas[0][2][1]>partidas[0][2][0]:
        pontosB=pontosB + 3
    elif partidas[0][2][0]==partidas[0][2][1]:
        pontosA=pontosA+1
        pontosB=pontosB+1
    if partidas[1][2][0]>partidas[1][2][1]:
        pontosA=pontosA+3
    elif partidas[1][2][1]>partidas[1][2][0]:
        pontosB=pontosB + 3
    elif partidas[1][2][0]==partidas[1][2][1]:
        pontosA=pontosA+1
        pontosB=pontosB+1
    return {partidas[0][0]:pontosA,partidas[0][1]:pontosB}