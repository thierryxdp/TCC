def pontos(x):
    gols_1 = x[0]
    gols_2 = x[1]
    if gols_1>gols2:
        return [3,0]
    if gols_2>gols1:
        return [0,3]
    if gols_1==gols_2:
        return [1,1]
def pontos_por_time(x):
    jg1 = x[0]
    jg2 = x[1]
    time1= jogo1[0]
    time2= jogo1[1]
    gols1jg1 = jogo1[2][0]
    gols2jg1 = jogo1[2][1]
    gols1jg2 = jogo2[2][0]
    gols2jg2 = jogo2[2][1]
    pontos_jg1 = pontos([gols1jg1 , gols2jg1])
    pontos_jg2 = pontos([gols1jg2 , gols2jg2])
    pontos_time1 = pontos_jg1[0] + pontos_jg2[1]
    pontos_time2 = pontos_jg1[1] + pontos_jg2[0]
    return {t2:pontos_time2, t1:pontos_time1