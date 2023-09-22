def pontos_por_time ([['time1','time2',[gols1,gols2]],['time2','time1',[gols3,gols4]]]):
    '''
    função que recebe uma lista de dois elementos, onde cada elemento é também uma lista
    que cmpleta, tem informações do número de gols, em dois jogos de futebol entre dois 
    times, no formato: [['time1','time2',[gols1,gols2]],['time2','time1',[gols3,gols4]]]
    lista -> dicionário
    '''
    if int(gols1) > int(gols2) and int(gols4) > int(gols3):
        return {'time1': 6,'time2': 0}