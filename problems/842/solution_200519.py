def pontos_por_time(jogos):
    '''Retorna os pontos de um time em um jogo de ida e volta, a
entrada deve ser dada como uma lista de dois elementos, cada
elemento conterá as informações do jogo de ida e o outro do
jogo de volta, como:[['time1','time2',[gols_time_1,gols_time2]],
['time2','time1',[gols_time2,gols_time1]]];
	lista -> dicionário'''
    ida=jogos[0]
    volta=jogos[1]
    t1=ida[0]
    t2=volta[0]
    gols_t1_ida=ida[2][0]
    gols_t2_ida=ida[2][1]
    gols_t1_volta=volta[2][1]
    gols_t2_volta=volta[2][0]
    if gols_t1_ida>gols_t2_ida and gols_t1_volta>gols_t2_volta:
        pt1=6
        pt2=0
    if gols_t1_ida>gols_t2_ida and gols_t1_volta==gols_t2_volta:
        pt1=4
        pt2=1
    if gols_t1_ida>gols_t2_ida and gols_t1_volta<gols_t2_volta:
        pt1=3
        pt2=3
    if gols_t1_ida==gols_t2_ida and gols_t1_volta>gols_t2_volta:
        pt1=4
        pt2=1
    if gols_t1_ida==gols_t2_ida and gols_t1_volta==gols_t2_volta:
        pt1=2
        pt2=2
    if gols_t1_ida==gols_t2_ida and gols_t1_volta<gols_t2_volta:
        pt1=1
        pt2=4
    if gols_t1_ida<gols_t2_ida and gols_t1_volta>gols_t2_volta:
        pt1=3
        pt2=3
    if gols_t1_ida<gols_t2_ida and gols_t1_volta==gols_t2_volta:
        pt1=1
        pt2=4
    if gols_t1_ida<gols_t2_ida and gols_t1_volta<gols_t2_volta:
        pt1=0
        pt2=6
    dicionario={t1:pt1, t2:pt2}
    return dicionario