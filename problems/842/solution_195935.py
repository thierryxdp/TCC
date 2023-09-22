def pontos_por_time(jogos):
    ji,jv = jogos
    p1 = 0
    p2 = 0
    pontuacao = {}
    
    if ji[1][0]==ji[1][1]:
        p1 += 1
        p2 += 1
    elif ji[ji[1][0]>ji[1][1]]:
        p1 += 3
    else:
        p2 += 3
        
    if jv[1][0]==jv[1][1]:
        p1 += 1
        p2 += 1
    elif jv[jv[1][0]>jv[1][1]]:
        p2 += 3
    else:
        p1 += 3
    pontuacao[ji[0][0]] = p1
    pontuacao[ji[0][1]] = p2
    return pontuacao