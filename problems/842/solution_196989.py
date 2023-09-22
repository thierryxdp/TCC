def pontos_por_time(lista):
    """
    	Retorna um dicionário com o nome dos times e suas respectivas pontuações finais
        list -> dict
    """
    jogo1=lista[0]
    jogo2=lista[1]
    ponto_time1_jogo1=jogo1[2][0]
    ponto_time2_jogo1=jogo1[2][1]
    ponto_time1_jogo2=jogo2[2][1]
    ponto_time2_jogo2=jogo2[2][0]
    ponto_time1_total=''
    ponto_time2_total=''
    if ponto_time1_jogo1>ponto_time2_jogo1:
        ponto_time1_total=ponto_time1_total+'3'
        ponto_time2_total=ponto_time2_total+'0'
    if ponto_time1_jogo1==ponto_time2_jogo1:
        ponto_time1_total=ponto_time1_total+'1'
        ponto_time2_total=ponto_time2_total+'1'
    if ponto_time1_jogo1<ponto_time2_jogo1:
        ponto_time1_total=ponto_time1_total+'0'
        ponto_time2_total=ponto_time2_total+'3'
    if ponto_time1_jogo2>ponto_time2_jogo2:
        ponto_time1_total=ponto_time1_total+'3'
        ponto_time2_total=ponto_time2_total+'0'
    if ponto_time1_jogo2==ponto_time2_jogo2:
        ponto_time1_total=ponto_time1_total+'1'
        ponto_time2_total=ponto_time2_total+'1'
    if ponto_time1_jogo2<ponto_time2_jogo2:
        ponto_time1_total=ponto_time1_total+'0'
        ponto_time2_total=ponto_time2_total+'3'
    ponto_time1_total=ponto_time1_total[0]+ponto_time1_total[1]
    ponto_time2_total=ponto_time2_total[0]+ponto_time2_total[1]
    dicio_fase={jogo1[0]:ponto_time1_total,jogo1[1]:ponto_time2_total}
    return dicio_fase