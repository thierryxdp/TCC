#def pontos_por_time(l):
    cormengo = l[0][0]
    flaminthians = l[0][1]

    gcormengo_jogo1 = l[0][2][0]
    gflaminthians_jogo1 = l[0][2][1]
    gcormengo_jogo2 = l[1][2][1]
    gflaminthians_jogo2 = l[1][2][0]

    pcormengo_jogo1 = 0
    pflaminthians_jogo1 = 0

    if gcormengo_jogo1 > gflaminthians_cormengo:
        pcormengo_jogo1 = pcormengo_jogo1 + 3
    elif gcormengo_jogo1 < gflaminthians_jogo1:
        pflaminthians_jogo1 = pflaminthians_jogo1 + 3
    elif gcormengo_jogo1 == gflaminthians_jogo1:
        pcormengo_jogo1 = pcormengo_jogo1 + 1
        pflaminthians_jogo1 = pflaminthians_jogo1 + 1

    pcormengo_jogo2 = 0
    ptime2_jogo2 = 0

    if gcormengo_jogo2 > gflaminthians_jogo2:
        pcormengo_jogo2 = pcormengo_jogo2 + 3
    elif gcormengo_jogo2 < gflaminthians_jogo2:
        pflaminthians_jogo2 = pflaminthians_jogo2 + 3
    elif gcormengo_jogo2 == gflaminthians_jogo2:
        pcormengo_jogo2 = pcormengo_jogo2 + 1
        pflaminthians_jogo2 = pflaminthians_jogo2 + 1

    pcormengo = pcormengo_jogo1 + pcormengo_jogo2
    pflaminthians = pflaminthians_jogo1 + pflaminthians_jogo2
    tabela = {cormengo:pcormengo, flaminthians:pflaminthians}