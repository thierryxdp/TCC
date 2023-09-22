def pontos_por_time(resultados_da_fase):
    """funcao que retorna um dicionario contendo os pontos conquistados, sendo a chave de acesso a string do nome do clube;
    list -> dict"""
    gols_time1_ida=resultados_da_fase[0][2][0]
    gols_time1_volta=resultados_da_fase[1][2][1]
    gols_time2_ida=resultados_da_fase[0][2][1]
    gols_time2_volta=resultados_da_fase[1][2][0]
    Time1=resultados_da_fase[0][0]
    Time2=resultados_da_fase[0][1]
    if gols_time1_ida>gols_time2_ida and gols_time1_volta>gols_time2_volta:
        pontuacao_time1=6
        pontuacao_time2=0
        return '{Time1:pontuacao_time1,Time2:pontuacao_time2}'
    elif gols_time1_ida<gols_time2_ida and gols_time1_volta<gols_time2_volta:
        pontuacao_time1=0
        pontuacao_time2=6
        return '{Time1:pontuacao_time1,Time2:pontuacao_time2}'
    elif gols_time1_ida==gols_time2_ida and gols_time1_volta>gols_time2_volta:
        pontuacao_time1=4
        pontuacao_time2=1
        return '{Time1:pontuacao_time1,Time2:pontuacao_time2}'
    elif gols_time1_ida==gols_time2_ida and gols_time1_volta<gols_time2_volta:
        pontuacao_time1=1
        pontuacao_time1=4
        return '{Time1:pontuacao_time1,Time2:pontuacao_time2}'
    elif gols_time1_ida==gols_time2_ida and gols_time1_volta==gols_time2_volta:
        pontuacao_time1=2
        pontuacao_time1=2
        return '{Time1:pontuacao_time1,Time2:pontuacao_time2}'