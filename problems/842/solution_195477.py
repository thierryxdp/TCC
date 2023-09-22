#placar[0] =placar[5]
#placar[1]=placar[4]

def pontos_por_time(placares):
    
    jogo1 = placares[0]
    gols1= jogo1[2]
    jogo2 = placares[1]
    gols2 = jogo2[2]
    pontuacao = {jogo1[1] : 0 ,jogo1[0] : 0 }
    
    if gols1[0]>gols1[1] and gols2[0]<gols2[1]:
        pontuacao[jogo1[0]] = 6

    elif gols1[0]<gols1[1] and gols2[0]>gols2[1]:
        pontuacao[ jogo1[1]]= 6
        
    elif gols1[0]==gols1[1] and gols2[0]==gols2[1]:
        pontuacao[jogo1[0]] = 2
        pontuacao[jogo1[1]] = 2
     
    elif gols1[0]>gols1[1] and gols2[0]>gols2[1]:
        pontuacao[jogo1[0], jogo1[1]] = 3
    
    return pontuacao