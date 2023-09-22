#Start your python function heredef 
def pontos_por_time(jogos):
    """uma função retornando um dicionário apresentado o número total de pontos de cada time dentro desses dois jogos;
    list, list -> dict"""
    jogo_ida = jogos[0]
    jogo_volta = jogos[1]
    time1 = jogo_ida[0]
    time2 = jogo_ida[1]
    pontos_t1 = 0
    pontos_t2 = 0
    gols_t1_ida = jogo_ida[2][0]
    gols_t1_volta = jogo_volta[2][1]
    gols_t2_ida = jogo_ida[2][1]
    gols_t2_volta = jogo_volta[2][0]
    if gols_t1_ida > gols_t2_ida:
        pontos_t1 += 3
    elif gols_t1_ida < gols_t2_ida:
        pontos_t2 += 3
    else:
        pontos_t1 += 1
        pontos_t2 += 1
    if gols_t1_volta > gols_t2_volta:
        pontos_t1 += 3
    elif gols_t1_volta < gols_t2_volta:
        pontos_t2 += 3
    else:
        pontos_t1 += 1
        pontos_t2 += 1
    return {time1:pontos_t1,time2:pontos_t2}