def pontos_por_time(lista):
    '''funcao que recebe como entrada duas listas, denominadas lista1 e lista2, que contem informacoes e de volta, respectivamente 
    do numero de gols nos jogos de ida e de volta, respectivamente e retorna um dicionario que mapeia
    o numero de pontos de um time na fase
    list -> dicionario'''
    gols_timeA_ida=lista[0][2][0]
    gols_timeB_ida=lista[0][2][1]
    gols_timeB_volta=lista[1][2][0]
    gols_timeA_volta=lista[1][2][1]
    timeA=lista[0][0]
    timeB=lista[0][1]
    if gols_timeA_ida>gols_timeB_ida and gols_timeB_volta<gols_timeA_volta:
        return {timeA:6, timeB:0}
    elif (gols_timeA_ida>gols_timeB_ida and gols_timeB_volta>gols_timeA_volta) or (gols_timeA_ida<gols_timeB_ida and gols_timeB_volta<gols_timeA_volta):
        return {timeA:3, timeB:3}
    elif (gols_timeA_ida>gols_timeB_ida and gols_timeB_volta==gols_timeA_volta) or (gols_timeA_ida==gols_timeB_ida and gols_timeB_volta<gols_timeA_volta): 
        return {timeA:4, timeB:1}
    elif gols_timeA_ida<gols_timeB_ida and gols_timeB_volta>gols_timeA_ida:
        return {timeA:0, timeB:6}
    elif (gols_timeA_ida<gols_timeB_ida and gols_timeB_volta==gols_timeA_volta) or (gols_timeA_ida==gols_timeB_ida and gols_timeB_volta>gols_timeA_volta):
        return {timeA:1, timeB:4}
    else:
    	return {timeA:2, timeB:2}