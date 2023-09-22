#placar[0] =placar[5]
#placar[1]=placar[4]

pontos_por_time(placares):
    
    placares[0] = jogo1
    jogo1[2]=gols1
    placares[1] = jogo2
    jogo2[2] = gols2
    pontuacao = {"jogo1[0]" : "saldo1","jogo1[1]" : "saldo2" }
    
    if gols1[0]>gols1[1]:
        pontuacao[ "saldo1"] =3
    if gols1[0]<gols1[1]:
        pontuacao[ "saldo2"]=3
    if gols1[0]==gols1[1]:
        pontuacao["saldo1", "saldo2"] = 1
    if gols2[0]>gols2[1]:
        pontuacao["saldo2"] =6
    if gols2[0]<gols2[1]:
        pontuacao["saldo1"]=6
    if gols2[0]==gols2[1]:
        pontuacao["saldo1","saldo2"] = int(pontuacao["saldo1","saldo2"]+3
return pontuacao