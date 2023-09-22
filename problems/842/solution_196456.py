def pontos_por_time(jogos):
    # pega os jogos
    primeiro = jogos[0]
    segundo = jogos[1]

    # pega a lista com os gols
    gol_pri = primeiro[2]
    gol_seg = segundo[2]

    # pega os gols da 1° partida
    golA = gol_pri[0]
    golB = gol_pri[1]

    # pega os gols da 2° partida
    golAA = gol_seg[1]
    golBB = gol_seg[0]

    # jogo 1
    if golA > golB :
        golA=3
        golB=0
    elif golA < golB:
        golA=0
        golB=3  
    else:
        golA=1
        golB=1


    # jogo 2
    if golAA > golBB:
        golAA=3
        golBB=0
    elif golAA < golBB:
        golAA=0
        golBB=3
    else:
        golAA=1
        golBB=1

    return {primeira[0]:golA+golAA, primeira[1]:golB+golBB}