def pontos_por_time(lista):
    '''funcao que recebe como entrada duas listas, denominadas lista1 e lista2, que contem informacoes e de volta, respectivamente 
    do numero de gols nos jogos de ida e de volta, respectivamente e retorna um dicionario que mapeia
    o numero de pontos de um time na fase
    list -> dicionario'''
    lista[0][2][0]=gols_timeA_ida
    lista[0][2][1]=gols_timeB_ida
    lista[1][2][0]=gols_timeB_volta
    lista[1][2][1]=gols_timeA_volta
    if gols_timeA_ida>gols_timeB_ida and gols_timeB_volta<gols_timeA_volta:
        return {lista[0][0]:6, lista[0][1]:0}
    elif (gols_timeA_ida>gols_timeB_ida and gols_timeB_volta>gols_timeA_volta) or (gols_timeA_ida<gols_timeB_ida and gols_timeB_volta<gols_timeA_volta):
        return {lista[0][0]:3, lista[0][1]:3}
    elif (gols_timeA_ida>gols_timeB_ida and gols_timeB_volta==gols_timeA_ida) or (gols_timeA_ida==gols_timeB_ida and gols_timeB_volta<gols_timeA_volta): 
        return {lista[0][0]:4, lista[0][1]:1}
    elif gols_timeA_ida<gols_timeB_ida and gols_timeB_volta>gols_timeA_ida:
        return {lista[0][0]:0, lista[0][1]:6}
    elif (gols_timeA_ida<gols_timeB_ida and gols_timeB_volta==gols_timeA_volta) or (gols_timeA_ida==gols_timeB_ida and gols_timeB_volta>gols_timeA_volta):
        return {lista[0][0]:1, lista[0][1]:4}
    else:
    	return {lista[0][0]:2, lista[0][1]:2}