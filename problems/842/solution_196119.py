def pontos_por_time (jogos):
    """Função que dada duas listas dos jogos de ida e de volta retorna o número total de pontos de cada time
    entrada:list
    saída:dict"""
    ida=jogos[0]
    volta=jogos[1]
    placar1=ida[2]
    placar2=volta[2]
    
   	if placar1[0] > placar1[1] and placar2[1] > placar2[0]:
        pt1=6
        pt2=0
    elif placar1[1]>placar1[0] and placar2[0]>placar2[1]:
        pt1=0
        pt2=6
    elif placar1[0]>placar1[1] and placar2[1]==placar2[0] or placar1[0]==placar1[1] and placar2[1]>placar2[0]:
        pt1=4
        pt2=1
    elif placar1[1]>placar1[0] and placar2[0]==placar2[1] or placar1[1]==placar1[0] and placar2[0]>placar2[1]:
        pt1=1
        pt2=4
    elif placar1[0]>placar1[1] and placar2[1]<placar2[0] or placar1[0]<placar1[1] and placar2[1]>placar2[0]:
        pt1=3
        pt2=3
    else:
        pt1=2
        pt2=2
    return {ida[0]:pt1,ida[1]:pt2}