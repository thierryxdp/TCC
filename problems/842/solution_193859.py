def pontos_por_time(confrontos):
    '''funcao que, dada uma lista com os placares de dois jogos entre o time1 e
    o time2, retorna um dicionario que mapeia a pontuacao das duas equipes apos
    os dois confrontos[time1, time2, lista com gols do time e gols do time2];
    list(str,str,list(int,int)),list->dict(str,int)'''
    time1=confrontos[0][0]
    time2=confrontos[0][1]
    gols_t1_jogo1=confrontos[0][2][0]
    gols_t2_jogo1=confrontos[0][2][1]
    gols_t1_jogo2=confrontos[1][2][1]
    gols_t2_jogo2=confrontos[1][2][0]
    jogo1=[time1,time2,[gols_t1_jogo1, gols_t2_jogo2]]
    jogo2=[time2,time1,[gols_t2_jogo2, gols_t1_jogo2]]   
    confrontos=[jogo1,jogo2]
    pontuacao={}
    if gols_t1_jogo1>gols_t2_jogo1 and gols_t1_jogo2>gols_t2_jogo2:
        pontuacao[time1]=(6)
        pontuacao[time2]=(0)
        return pontuacao
    elif gols_t1_jogo1<gols_t2_jogo1 and gols_t1_jogo2<gols_t2_jogo2:
        pontuacao[time1]=(0)
        pontuacao[time2]=(6) 
        return pontuacao
    elif (gols_t1_jogo1>gols_t2_jogo1 and gols_t1_jogo2==gols_t2_jogo2)or(gols_t1_jogo1==gols_t2_jogo1 and gols_t1_jogo2>gols_t2_jogo2):
        pontuacao[time1]=(4)
        pontuacao[time2]=(1) 
        return pontuacao 
    elif (gols_t1_jogo1>gols_t2_jogo1 and gols_t1_jogo2<gols_t2_jogo2)or(gols_t1_jogo1<gols_t2_jogo1 and gols_t1_jogo2>gols_t2_jogo2):
        pontuacao[time1]=(3)
        pontuacao[time2]=(3) 
        return pontuacao 
    elif (gols_t1_jogo1<gols_t2_jogo1 and gols_t1_jogo2==gols_t2_jogo2)or(gols_t1_jogo1==gols_t2_jogo1 and gols_t1_jogo2<gols_t2_jogo2):
        pontuacao[time1]=(1)
        pontuacao[time2]=(4) 
        return pontuacao
    elif gols_t1_jogo1==gols_t2_jogo1 and gols_t1_jogo2==gols_t2_jogo2:
        pontuacao[time1]=(2)
        pontuacao[time2]=(2) 
        return pontuacao