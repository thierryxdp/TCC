def pontos_por_time (lista):
    '''
    função que recebe uma lista de dois elementos, onde cada elemento é também uma lista
    que cmpleta, tem informações do número de gols, em dois jogos de futebol entre dois 
    times, no formato: [['time1','time2',[gols1,gols2]],['time2','time1',[gols3,gols4]]]
    lista -> dicionário
    '''
    lista = [[lista1]+[lista2]]
    lista1 = [time1, time2, [gols1, gols2]]
    lista2 = [time2, time1, [gols3, gols4]]
    if int(gols1) > int(gols2) and int(gols4) > int(gols3):
        return {'time1': 6, 'time2': 0}
    elif int(gols2) > int(gols1) and int(gols3) > int(gols4):
        return {'time2':6, 'time1':0}
    elif int(gols1) > int(gols2) and int(gols3) == int(gols4):
        return {'time1':4, 'time2':1}
    elif int(gols2) > int(gols1) and int(gols4) == int(gols3):
        return {'time2':4, 'time1':1}
    elif int(gols1) > int(gols2) and int(gols3) > int(gols4) or int(gols1) < int(gols2) and int(gols3) < int(gols4):
        return {'time1':3, 'time2':3}
    else:
        return {'time1':2, 'time2':2}