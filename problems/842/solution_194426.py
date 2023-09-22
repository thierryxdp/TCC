def pontos_por_time(infos):
    '''Função que retorna um dicionário com o total de pontos de cada time, dadas as informações sobre os jogos de ida e de volta.
    list->dict'''
    jogo_ida,jogo_volta=infos
    time1,time2,placar_ida=jogo_ida
    time2,time1,placar_volta=jogo_volta
    pontos_time1=0
    pontos_time2=0
    if (placar_ida[0]>placar_ida[1]):
        pontos_time1=pontos_time1 + 3
    elif(placar_ida[0]<placar_ida[1]):
         pontos_time2=pontos_time2 + 3
    else:
        pontos_time1=pontos_time1 + 1
        pontos_time2=pontos_time2 + 1
    if (placar_volta[1]>placar_volta[0]):
        pontos_time1=pontos_time1 + 3
    elif(placar_volta[1]<placar_volta[0]):
         pontos_time2=pontos_time2 + 3
    else:
        pontos_time1=pontos_time1 + 1
        pontos_time2=pontos_time2 + 1
   	return {time1:pontos_time1,time2:pontos_time2}