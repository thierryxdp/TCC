#Start your python f  unc tion heredef pontos_por_time(jogos):
    'Retorna a pontuação dos times dado o numero total de jogos e sua pontuação em cada um'
    'list,list--dict'
    jogo_ida=jogo[0]
    jogo_volta=jogos[1]
    time1=jogo_ida[0]
    time2=jogoida[1]
    pontos_time1=0
    pontos_time2=0
    gols_time1_ida= jogo_ida[2][0]
    gols_time1_volta=jogo_volta[2][1]
    gols_time2_ida=jogo_ida[2][1]
    gols_time2_volta=jogo_volta[2][1]
    if gols_time1_ida>gols_time2_ida:
        pontos_time1+=3
    elif gols_time1_ida<gols_time2_ida:
        pontos_time2+=3
    else:
        pontos_time1+=1
        pontos_time2+=1
    if gols_time1_volta<gols_time2_volta:
        pontos_time2+=3
    elif gols_time2_volta>gols_time2_volta:
        pontos_time1+=3
    else:
        pontos_time1+=1
        pontos_time2+=1
    return {time1:pontos_time1,time2:pontos_time2}