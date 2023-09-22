def pontuacao(placar):
    if placar[0] == placar[1]:
        return 1,1
    elif placar[0] > placar[1]:
        return 3,0
    else:
        return 0,3

def pontos_por_time(jogos):
    
    nome1 = jogos[0][0]
    nome2 = jogos[1][0]
    
    placar1 = jogos[0][2]
    placar2 = jogos[1][2]
    
    p1,p2 = pontuacao(placar1)
    p3,p4 = pontuacao(placar2)
    
    return {nome1:p1+p4, nome2:p2+p3}