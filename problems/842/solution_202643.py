def pontos_por_time(s):

    #Jogos 
    j1 = s[0]
    j2 = s[1]

    #Times
    t1 = j1[0]
    t2 = j1[1]

    #Gols primeira partida
    g = j1[2]
    gT1 = g[0]
    gT2 = g[1]

    #Gols segunda partida
    g2 = j2[2]
    g2T1 = g2[1]
    g2T2 = g2[0]

    #Placar de pontos
    p1T1 = p1T2 = p2T1 = p2T2 = 0

    #Placar da primeira rodada
    if gT1 > gT2:
        p1T1 = 3
        p1T2 = 0
    elif gT1 == gT2:
        p1T1 = 1
        p1T2 = 1
    elif gT1 < gT2:
        p1T1 = 0
        p1T2 = 3
        
    #Pontos da segunda rodada 
    if g2T1 > g2T2:
        p2T1 = 3
        p2T2 = 0
    elif g2T1 == g2T2:
        p2T1 = 1
        p2T2 = 1
    elif g2T1 < g2T2:
        p2T1 = 0
        p2T2 = 3

    #Pontos Totais 
    ptT1 = p1T1 + p2T2
    ptT2 = p1T2 + p2T2

    return {
        t1: ptT1, t2: ptT2
    }