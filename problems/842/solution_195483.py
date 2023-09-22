def pontos_por_time(placares):
    """ Apos informar um placar em forma de lista a funcao
    ira retornar um dicionario contendo o nome dos times
    e a pontuacao deles num campeonato. Essa lista sera
    composta por duas listas sendo elas o jogo de ida
    e de volta,- respectivamente -,  dos times no campeonato.
    [[str,str, list],[str,str,list]] -> dictionary """
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
     
    elif (gols1[0]>gols1[1] and gols2[0]>gols2[1]) or (gols1[0]<gols1[1] and gols2[0]<gols2[1]):
        pontuacao[jogo1[0]] = 3
        pontuacao[jogo1[1]] = 3
        
    elif (gols1[0]==gols1[1] and gols2[1]>gols2[0]) or (gols1[0]>gols1[1] and gols2[0]==gols2[1]):
        pontuacao[jogo1[0]] = 4
        pontuacao[jogo1[1]] = 1
        
    elif (gols1[0]==gols1[1] and gols2[0]>gols2[1]) or (gols1[1]>gols1[0] and gols2[0]==gols2[1]):
        pontuacao[jogo1[0]] = 1
        pontuacao[jogo1[1]] = 4
    return pontuacao