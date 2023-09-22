def pontos_por_time(jogos):
#Funcao que calcula os pontos dos jogos dependendo do resultado
    pontos1 = 0
    pontos2 = 0
    ida = jogos[0]
    volta = jogos[1]
    placar1 = ida[2]
    placar2 = volta[2]
    if placar1[0] == placar1[1]:
#Se for empate no jogo 1,ganha 1 ponto
        pontos1 += 1
        pontos2 += 1
    if placar2[0] == placar2[1]:
#Se for empate no jogo 2,ganha 1 ponto
        pontos1 += 1
        pontos2 += 1   
    if placar1[0] > placar1[1]:
#Se for vitoria para o time 1, no jogo 1, ganha 3 pontos.
        pontos1 += 3
    if placar1[1] > placar1[0]:
#Se for vitoria para o time 2, no jogo 1, ganha 3 pontos.
        pontos2 += 3
    if placar2[0] > placar2[1]:
#Se for vitoria para o time 1, no jogo 2, ganha 3 pontos.
        pontos1 += 3
    if placar2[1] > placar2[0]:
#Se for vitoria para o time 2, nogo jogo 2, ganha 3 pontos.
        pontos2 += 3

    lista=[(ida[0],pontos1),(ida[1],pontos2)]
    dicionario=dict(lista)
    return dicionario