def pontos_por_time(jogo1,jogo2):
    '''funcao que, dada uma lista com os placares de dois jogos entre Cormengo e
    Flamínthians, retorna um dicionario que mapeia a pontuacao das duas equipes apos os
    dois confrontos[time1, time2, lista com gols do time e gols do time2];
    list(str,str,list(int,int)),list->dict(str,int)'''
    time1=jogo1[0]
    time2=jogo2[0]
    gols_t1_jogo1=jogo1[2][0]
    gols_t2_jogo1=jogo1[2][1]
    gols_t1_jogo2=jogo2[2][1]
    gols_t2_jogo2=jogo2[2][0]
    if gols_t1_jogo1>gols_t2_jogo1 and gols_t1_jogo2>gols_t2_jogo2:
        return pontos_time1==6, pontos_time2==0
    elif gols_t1_jogo1<gols_t2_jogo1 and gols_t1_jogo2<gols_t2_jogo2:
        return pontos_time1==0, pontos_time2==6
    elif (gols_t1_jogo1>gols_t2_jogo1 and gols_t1_jogo2==gols_t2_jogo2)or(gols_t1_jogo1==gols_t2_jogo1 and gols_t1_jogo2>gols_t2_jogo2):
        return pontos_time1==4, pontos_time2==1
    elif (gols_t1_jogo1>gols_t2_jogo1 and gols_t1_jogo2<gols_t2_jogo2)or(gols_t1_jogo1<gols_t2_jogo1 and gols_t1_jogo2>gols_t2_jogo2):
        return pontos_time1==3, pontos_time2==3
    elif (gols_t1_jogo1<gols_t2_jogo1 and gols_t1_jogo2==gols_t2_jogo2)or(gols_t1_jogo1==gols_t2_jogo1 and gols_t1_jogo2<gols_t2_jogo2):
        return pontos_time1==1, pontos_time2==4
    else:
        return pontos_time1==2, pontos_time2==2
    return {time1:pontos_time1, time2:pontos_time2}