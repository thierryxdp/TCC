def pontos_por_time(lista):
    '''Recebe uma lista de dois elementos com informações do número de gols
    em dois jogos de futebol entre dois times (ida e volta).
    list -> dict'''
    dados = {'time1': lista[0][0],
             'time2': lista[1][0],
             'gols_time1_j1': lista[0][2][0],
             'gols_time1_j2': lista[1][2][0],
             'gols_time2_j1': lista[0][2][1],
             'gols_time2_j2': lista[1][2][1],
             'empate_time1': lista[0]} 
    total_time1 = dados['gols_time1_j1'] + dados['gols_time1_j2'] 

    pontos_time2_jogo1 = dados['gols_time2_j1'] 
    pontos_time2_jogo2 = dados['gols_time2_j2'] 
    total_time2 = pontos_time2_jogo1 + pontos_time2_jogo2
    return dados['time1'],pontos_time1_jogo1,dados['time2'],pontos_time1_jogo2,