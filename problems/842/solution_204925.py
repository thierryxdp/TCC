[07:33, 20/07/2022] Limoin Ufrj (João ): g1 = x[0]
    jg2 = x[1]
    time1= jg1[0]
    time2= jg1[1]
    gols1jg1 = jg1[2][0]
    gols2jg1 = jg1[2][1]
    gols1jg2 = jg2[2][0]
    gols2jg2 = jg2[2][1]
[07:33, 20/07/2022] Limoin Ufrj (João ): pontos_jg1 = pontos([gols1jg1 , gols2jg1])
    pontos_jg2 = pontos([gols1jg2 , gols2jg2])
    pontos_time1 = pontos_jg1[0] + pontos_jg2[1]
    pontos_time2 = pontos_jg1[1] + pontos_jg2[0]
    return {time2:pontos_time2, time1:pontos_time1}
#Start your python function here