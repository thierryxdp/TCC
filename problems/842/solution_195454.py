#placar[0] =placar[5]
#placar[1]=placar[4]

def pontos_por_time(placares):
    
    jogo1 = placares[0]
    gols1= jogo1[2]
    jogo2 = placares[1]
    gols2 = jogo2[2]
    pontuacao = {jogo1[0] : 0 ,jogo1[1] : 0 }
    
    if gols1[0]>gols1[1] and gols2[0]<gols2[1]:
        pontuacao[ "saldo1"] =int(pontuacao[ "saldo1"]) + 6

    elif gols1[0]<gols1[1] and gols2[0]>gols2[1]:
        pontuacao[ "saldo2"]= int(pontuacao[ "saldo2"]) + 6

        
    elif gols1[0]==gols1[1] and gols2[0]==gols2[1]:
        pontuacao["saldo1", "saldo2"] = 3

    elif gols2[0]>gols2[1]:
        pontuacao["saldo2"] = int(pontuacao["saldo2"]) + 3
    return pontuacao