def pontos_por_time(lista):
    """Função que pegas os valores da lista de entrada, e vê qual time ganhou ou empatou e o derrotado, e calcula a pontuação baseada
    no resultado da partida, transformando em um dicionário de retorno
    list, list→dicti"""
    time1_ida=lista[0] [0]
    time2_ida=lista[0] [1]
    gols_ida_time1=lista [0] [2] [0]
    gols_ida_time2=lista [0] [2] [1]
    time1_volta=lista [1] [1]
    time2_volta=lista [1] [0]
    gols_volta_time1=lista [1] [2] [1]
    gols_volta_time2=lista [1] [2] [0]
	if gols_ida_time1 > gols_ida_time2:
        pontos_time1=3
        pontos_time2=0
    if gols_ida_time1 < gols_ida_time2:
		pontos_time2=3
        pontos_time1=0
    if gols_ida_time1==gols_ida_time2:
        pontos_time1=1
        pontos_time2=1
    if gols_volta_time1 > gols_volta_time2:
        pontos_time1_v=3
        pontos_time2_v=0
    if gols_volta_time1 < gols_volta_time2:
        pontos_time2_v=3
        pontos_time1_v=0
    if gols_volta_time1 == gols_volta_time2:
        pontos_time1_v=1
        pontos_time2_v=1
    resultado1=pontos_time1+pontos_time1_v
    resultado2=pontos_time2+pontos_time2_v
    return {str(time1_ida):resultado1, str(time2_ida):resultado2}