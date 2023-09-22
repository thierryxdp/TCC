def pontos_por_time(lista_com_jogos):
    '''Funcao que retorna um dicionario cujos mapeamentos sao: <nome do time> -> <numero total de pontos na fase>. Os parametros 'jogo_de_ida' e 'jogo_de_volta' sao listas no seguinte formato:
    [TimeVencedor, OutroTime,[Gols_TimeVencedor, Gols_OutroTime]]. Em casos de empate, a ordem dos dois primeiros elementos da lista nao fara diferenca.
    [str,str[int,int]], [str,str[int,int]] -> dict'''

#Separei as listas para poder trabalhar melhor com elas durante o código
    jogo_de_ida = lista_com_jogos[0]
    times = jogo_de_ida[0:2]
    placar1 = jogo_de_ida[2]

    
    jogo_de_volta = lista_com_jogos[1]
    placar2 = jogo_de_volta[2]
    
    PontosTime1 = []
    PontosTime2 = []
    
    if placar1[0]>placar1[1] and placar2[0]<placar2[1]:
        PontosTime1 = [6]
        PontosTime2 = [0]
    elif placar1[0]<placar1[1] and placar2[0]>placar2[1]:
        PontosTime2 = [6]
        PontosTime1 = [0]
    elif placar1[0]==placar1[1] and placar2[0]==placar2[1]:
        PontosTime1 = [2]
        PontosTime2 = [2]
    elif placar1[0]>placar1[1] and placar2[0]>placar2[1]:
        PontosTime1 = [3]
        PontosTime2 = [3]
    elif placar1[0]>placar1[1] and placar2[0]==placar2[1]:
        PontosTime1 = [4]
        PontosTime2 = [1]
    elif placar2[0]<placar2[1] and placar1[0]==placar1[1]:
        PontosTime2 = [4]
        PontosTime1 = [1]

    placar = {times[0]: PontosTime1[0], times[1]: PontosTime2[0]}
    return placar