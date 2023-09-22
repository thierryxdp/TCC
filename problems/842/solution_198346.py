def pontos_por_time (jogos):
    '''
    função que recebe uma lista de dois elementos, onde cada elemento é também uma lista
    que cmpleta, tem informações do número de gols, em dois jogos de futebol entre dois 
    times, no formato: [['time1','time2',[gols1,gols2]],['time2','time1',[gols3,gols4]]]
    lista -> dicionário
    '''
    if int(jogos[0][2][0]) > int(jogos[0][2][1]) and int(jogos[1][2][1]) > int(jogos[1][2][0]):
        return {jogos[0][0]: 6, jogos[0][1]: 0}
    if int(jogos[0][2][1]) > int(jogos[0][2][0]) and int(jogos[1][2][0]) > int(jogos[1][2][1]):
        return {jogos[0][1]:6, jogos[0][0]:0}
    if int(jogos[0][2][0]) > int(jogos[0][2][1]) and int(jogos[1][2][0]) == int(jogos[1][2][1]):
        return {jogos[0][0]:4, jogos[0][1]:1}
    if int(jogos[0][2][1]) > int(jogos[0][2][0]) and int(jogos[1][2][1]) == int(jogos[1][2][0]):
        return {jogos[0][1]:4, jogos[0][0]:1}
    if int(jogos[0][2][0]) > int(jogos[0][2][1]) and int(jogos[1][2][0]) > int(jogos[1][2][1]) or int(jogos[0][2][0]) < int(jogos[0][2][1]) and int(jogos[1][2][0]) < int(jogos[1][2][1]):
        return {jogos[0][0]:3, jogos[0][1]:3}
    if int(jogos[0][2][0]) == int(jogos[0][2][1]) and int(jogos[1][2][0]) == int(jogos[1][2][1]):
        return {jogos[0][0]:2, jogos[0][1]:2}
    if int(jogos[0][2][0]) == int(jogos[0][2][1]) and int(jogos[1][2][0]) < int(jogos[1][2][1]):
        return {jogos[0][0]:4, jogos[0][1]:1}#Start your python function here