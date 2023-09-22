def pontos_por_time(lista1):
    """ Função que retorna os pontos de um time em dois jogos no campeonato
    list,list - dicionário """
    time1=(lista1[0])[0]
    time2=(lista1[0])[1]
    jogo1=(lista1[0])[2]
    jogo2=(lista1[1])[2]
    if jogo1[0]==jogo1[1]:
        pontuacao11=1
        pontuacao21=1
    elif jogo1[0]>jogo1[1]:
        pontuacao11=3
        pontuacao21=0
    else:
        pontuacao11=0
        pontuacao21=3
    if jogo2[0]==jogo2[1]:
        pontuacao12=1
        pontuacao22=1
    elif jogo2[0]>jogo2[1]:
        pontuacao12=0
        pontuacao22=3
    else:
        pontuacao12=3
        pontuacao22=0
    
    return {time1:(pontuacao11+pontuacao12),time2:(pontuacao21+pontuacao22)}