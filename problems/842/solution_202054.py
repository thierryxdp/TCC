def pontos_por_time(s):

    #Jogos
    j1 = s[0]
    j2 = s[1]

    #Times
    t1 = j1[0]
    t2 = j1[1]
    
    #Gols da primeira rodada
    g1 = j1[2]
    Fla = g1[0]
    Cor = g1[1]

    #Gols da segunda rodada
    g2 = j2[2]
    Fla2 = g2[0]
    Cor2 = g2[1]

    #Pontos da primeira rodada
    p1Fla = p1Cor = 0

    if Fla > Cor:
        p1Fla = 3
        p1Cor = 0
    elif Fla == Cor:
        p1Fla = 1
        p1Cor = 1
    elif Fla < Cor:
        p1Fla = 0
        p1Cor = 3

    #Pontos da segunda rodada
    p2Fla = p2Cor = 0

    if Fla2 > Cor2:
        p2Fla = 3
        p2Cor = 0
    elif Fla2 == Cor2:
        p2Fla = 1
        p2Cor = 1
    elif Fla2 < Cor2:
        p2Fla = 0
        p2Cor = 3
    
    #Pontos totais
    ptFla = p1Fla + p2Fla
    ptCor = p1Cor + p2Cor

    return {
        t2: ptFla, t1: ptCor 
    }