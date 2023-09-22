#Questao 2
def pontos_por_time('nome_time1','nome_time2', L1, L2):

    '''
Pontos do time na fase
    '''
    #Primeira partida
    if ponto_time1_L1==ponto_time2_L1:
        ponto_time1_jogo1=1
        ponto_time2_jogo1=1
    if ponto_time1_partida1>ponto_time2_partida1:
        ponto_time1_jogo1=3
        ponto_time2_jogo1=0

    #Segunda partida
    if ponto_time1_partida2==ponto_ti5Fme2_partida2:
        ponto_time1_jogo2=1
        ponto_time2_jogo2=1
    if ponto_time1_partida2>ponto_time2_partida2:
        ponto_time1_jogo2=3
        ponto_time2_jogo2=0

    #Final partidas
    if nome_time1_partida1==nome_time1_partida2:
        total_time1=ponto_time1_jogo1+ponto_time1_jogo2
        total_time2=ponto_time2_jogo1+ponto_time2_jogo2
        return {nome_time1:total_time1,
                nome_time2:total_time2}
    elif nome_time1_partida1!=nome_time1_partida2:
        total_time1=ponto_time1_jogo1+ponto_time1_jogo2
        total_time2=ponto_time2_jogo1+ponto_time2_jogo2
        return {nome_time1:total_time1,
                nome_time2:total_time2}