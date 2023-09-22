def pontos(x):
    gols1= x[0]
    gols2= x[1]
    if gols1>gols2:
        return [3,0]
    if gols1<gols2:
        return [0,3]
    if gols1==gols2:
        return [1,1]
def pontos_por_time(x):
    jg1 = x[0]
    jg2 = x[1]
    t1 = jg1[0]
    t2 = jg1[1]
    gols1jg1 = jg1[2][0]
    gols2jg1 = jg1[2][1]
    gols1jg2 = jg2[2][0]
    gols2jg2 = jg2[2][1]
    pontosjg1 = pontos([gols1jg1 , gols2jg1])
    pontosjg2 = pontos([gols1jg2 , gols2jg2])
    pontost1= pontosjg1[0] + pontosjg2[1]
    pontost2= pontosjg1[1] + pontosjg2[0]
    return {t2:pontost2, t1:pontost1}