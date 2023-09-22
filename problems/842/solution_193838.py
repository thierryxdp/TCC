def pontos_por_time(confrontos):
    '''funcao que, dada uma lista com os placares de dois jogos entre o time1 e
    o time2, retorna um dicionario que mapeia a pontuacao das duas equipes apos
    os dois confrontos[time1, time2, lista com gols do time e gols do time2];
    list(str,str,list(int,int)),list->dict(str,int)'''
    time1=confrontos[0]
    time2=confrontos[1]
    gols_t1_jogo1=confrontos[0][2][0]
    gols_t2_jogo1=confrontos[0][2][1]
    gols_t1_jogo2=confrontos[1][2][1]
    gols_t2_jogo2=confrontos[1][2][0]
    jogo1=[time1,time2,[gols_t1_jogo1, gols_t2_jogo2]]
    jogo2=[time2,time1,[gols_t2_jogo2, gols_t1_jogo2]]   
    confrontos=[jogo1,jogo2]
    if gols_t1_jogo1>gols_t2_jogo1 and gols_t1_jogo2>gols_t2_jogo2:
        return (time1:6, time2:0) 
    elif gols_t1_jogo1<gols_t2_jogo1 and gols_t1_jogo2<gols_t2_jogo2:
        return (time1:0, time2:6) 
    elif (gols_t1_jogo1>gols_t2_jogo1 and gols_t1_jogo2==gols_t2_jogo2)or(gols_t1_jogo1==gols_t2_jogo1 and gols_t1_jogo2>gols_t2_jogo2):
        return (time1:4, time2:1) 
    elif (gols_t1_jogo1>gols_t2_jogo1 and gols_t1_jogo2<gols_t2_jogo2)or(gols_t1_jogo1<gols_t2_jogo1 and gols_t1_jogo2>gols_t2_jogo2):
        return (time1:3, time2:3) 
    elif (gols_t1_jogo1<gols_t2_jogo1 and gols_t1_jogo2==gols_t2_jogo2)or(gols_t1_jogo1==gols_t2_jogo1 and gols_t1_jogo2<gols_t2_jogo2):
        return (time1:1, time2:4)
    elif gols_t1_jogo1==gols_t2_jogo1 and gols_t1_jogo2==gols_t2_jogo2:
        return (time1:2, time2:2)